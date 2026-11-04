"""Normalização e validação de uplinks do The Things Stack.

Contrato: ver docs/contrato_dados.md.
"""
import math
from dataclasses import dataclass, field


class MensagemInvalida(Exception):
    """Mensagem sem a informação mínima de identificação."""


# PROVISÓRIO: marcadores de posição. Substituir pelos campos CONFIRMADOS do
# sensor quando houver uma mensagem real (não inferir pelo nome comercial).
RULES = {
    "grandeza_a": {"unit": "u_a", "min": 0.0, "max": 100.0},
    "grandeza_b": {"unit": "u_b", "min": 0.0, "max": 100.0},
}


@dataclass(frozen=True)
class Observation:
    event_key: str
    device_id: str
    quantity: str
    value: float
    unit: str
    quality: str
    received_at: str
    measured_at: str | None
    time_origin: str
    source: str        # "real" | "synthetic"
    acquisition: str   # "live" | "replay"


@dataclass(frozen=True)
class Issue:
    quantity: str
    status: str        # "ausente" | "invalido"
    reason: str


@dataclass
class ValidationResult:
    event_key: str
    device_id: str
    observations: list = field(default_factory=list)
    issues: list = field(default_factory=list)


def build_event_key(device_id: str, session_key_id: str, f_cnt: int) -> str:
    """Chave de reprocessamento: dispositivo + sessão + contador de trama."""
    return f"{device_id}|{session_key_id}|{f_cnt}"


def parse_uplink(raw: dict, source: str = "real", acquisition: str = "live") -> ValidationResult:
    """Valida um uplink. Levanta MensagemInvalida só se faltar a identificação."""
    try:
        device_id = raw["end_device_ids"]["device_id"]
        msg = raw["uplink_message"]
        received_at = raw.get("received_at") or msg["received_at"]
    except (KeyError, TypeError) as exc:
        raise MensagemInvalida(f"identificação em falta: {exc!r}") from exc

    f_cnt = msg.get("f_cnt", 0)   # o TTS pode omitir o campo quando vale 0
    session = msg.get("session_key_id", "")
    key = build_event_key(device_id, session, f_cnt)

    result = ValidationResult(event_key=key, device_id=device_id)
    decoded = msg.get("decoded_payload") or {}

    for quantity, rule in RULES.items():
        value = decoded.get(quantity)
        if value is None:
            result.issues.append(Issue(quantity, "ausente", "campo não presente na mensagem"))
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            result.issues.append(Issue(quantity, "invalido", f"valor não numérico: {value!r}"))
            continue
        if not rule["min"] <= value <= rule["max"]:
            result.issues.append(Issue(
                quantity, "invalido",
                f"{value} fora do intervalo [{rule['min']}, {rule['max']}] {rule['unit']}"))
            continue
        result.observations.append(Observation(
            event_key=key, device_id=device_id, quantity=quantity,
            value=float(value), unit=rule["unit"], quality="ok",
            received_at=received_at, measured_at=None,
            time_origin="ttn.received_at", source=source, acquisition=acquisition))
    return result

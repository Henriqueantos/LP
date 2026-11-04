"""Orquestração partilhada pelo consumidor e pela reprodução."""
import json
import logging
from datetime import datetime, timezone

from .validation import MensagemInvalida, parse_uplink

log = logging.getLogger(__name__)


def process_message(store, topic, payload, acquisition="live", source="real"):
    """Processa uma mensagem sem nunca levantar exceção por dados maus.

    Devolve o nº de observações novas, ou None se a mensagem foi rejeitada.
    """
    ts = datetime.now(timezone.utc).isoformat()
    try:
        result = parse_uplink(json.loads(payload), source=source, acquisition=acquisition)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        store.log_raw(topic, payload, ts, acquisition, source, None,
                      "invalida", f"JSON inválido: {exc}")
        log.warning("JSON inválido rejeitado")
        return None
    except MensagemInvalida as exc:
        store.log_raw(topic, payload, ts, acquisition, source, None,
                      "invalida", str(exc))
        log.warning("Mensagem rejeitada: %s", exc)
        return None

    raw_id = store.log_raw(topic, payload, ts, acquisition, source,
                           result.event_key, "processada", None)
    new = store.save_result(raw_id, result)
    log.info("evento=%s novas=%d problemas=%d", result.event_key, new, len(result.issues))
    return new

import json

import pytest

from observatorio.validation import MensagemInvalida, parse_uplink


def test_mensagem_valida(make_msg):
    r = parse_uplink(json.loads(make_msg()))
    assert len(r.observations) == 2
    assert not r.issues


def test_campo_ausente_nao_vira_zero(make_msg):
    r = parse_uplink(json.loads(make_msg(grandeza_a=10.0)))
    assert [o.quantity for o in r.observations] == ["grandeza_a"]
    assert r.issues[0].status == "ausente"


def test_valor_fora_de_intervalo_e_invalido(make_msg):
    r = parse_uplink(json.loads(make_msg(grandeza_a=999, grandeza_b=50)))
    assert r.issues[0].status == "invalido"
    assert len(r.observations) == 1


def test_valor_nao_numerico(make_msg):
    r = parse_uplink(json.loads(make_msg(grandeza_a="abc", grandeza_b=50)))
    assert r.issues[0].status == "invalido"


def test_sem_identificacao_levanta():
    with pytest.raises(MensagemInvalida):
        parse_uplink({"foo": 1})

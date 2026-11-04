import json

from observatorio.processing import process_message


def test_json_invalido_nao_interrompe(store, make_msg):
    assert process_message(store, "t", b"{isto nao e json") is None
    assert process_message(store, "t", make_msg()) == 2   # a seguinte é processada
    assert store.count("raw_messages") == 2


def test_idempotencia(store, make_msg):
    msg = make_msg()
    assert process_message(store, "t", msg) == 2
    assert process_message(store, "t", msg) == 0           # mesmo evento: 0 novas
    assert store.count("observations") == 2
    assert store.count("raw_messages") == 2                # as tentativas repetem-se


def test_mesmo_valor_evento_diferente_conta(store, make_msg):
    a = json.loads(make_msg())
    b = json.loads(make_msg())
    b["uplink_message"]["f_cnt"] = 8                       # valores iguais, evento novo
    process_message(store, "t", json.dumps(a).encode())
    process_message(store, "t", json.dumps(b).encode())
    assert store.count("observations") == 4


def test_replay_preserva_origem_real(store, make_msg):
    process_message(store, "replay", make_msg(), acquisition="replay", source="real")
    row = store.conn.execute("SELECT source, acquisition FROM observations").fetchone()
    assert row == ("real", "replay")


def test_sintetico_fica_assinalado(store, make_msg):
    process_message(store, "replay", make_msg(), acquisition="replay", source="synthetic")
    row = store.conn.execute("SELECT DISTINCT source FROM observations").fetchone()
    assert row == ("synthetic",)

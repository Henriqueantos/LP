import copy
import json

import pytest

from observatorio.storage import Store

BASE = {
    "end_device_ids": {"device_id": "sensor-sintetico-01"},
    "received_at": "2026-11-04T10:00:00.000Z",
    "uplink_message": {
        "session_key_id": "sessao-teste",
        "f_cnt": 7,
        "decoded_payload": {"grandeza_a": 10.0, "grandeza_b": 50.0},
    },
}


@pytest.fixture
def make_msg():
    def _make(**decoded_override):
        m = copy.deepcopy(BASE)
        if decoded_override:
            m["uplink_message"]["decoded_payload"] = decoded_override
        return json.dumps(m).encode()
    return _make


@pytest.fixture
def store():
    return Store(":memory:")

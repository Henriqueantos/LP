"""Persistência (SQLite no M1).

A interface da classe Store mantém-se se a base de dados mudar no M2.
"""
import sqlite3
import threading

SCHEMA = """
CREATE TABLE IF NOT EXISTS raw_messages (
    id INTEGER PRIMARY KEY,
    consumer_received_at TEXT NOT NULL,
    topic TEXT,
    payload TEXT NOT NULL,
    acquisition TEXT NOT NULL,
    source TEXT NOT NULL,
    event_key TEXT,
    status TEXT NOT NULL,
    reason TEXT
);
CREATE TABLE IF NOT EXISTS observations (
    id INTEGER PRIMARY KEY,
    event_key TEXT NOT NULL,
    device_id TEXT NOT NULL,
    quantity TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    quality TEXT NOT NULL,
    received_at TEXT NOT NULL,
    measured_at TEXT,
    time_origin TEXT NOT NULL,
    source TEXT NOT NULL,
    acquisition TEXT NOT NULL,
    UNIQUE (event_key, quantity)
);
CREATE TABLE IF NOT EXISTS rejections (
    id INTEGER PRIMARY KEY,
    raw_message_id INTEGER NOT NULL,
    quantity TEXT,
    status TEXT NOT NULL,
    reason TEXT NOT NULL
);
"""


class Store:
    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self._lock = threading.Lock()
        with self._lock, self.conn:
            self.conn.executescript(SCHEMA)

    def log_raw(self, topic, payload, consumer_ts, acquisition, source,
                event_key, status, reason):
        """Regista TODA a tentativa (as tentativas podem repetir-se)."""
        if isinstance(payload, bytes):
            payload = payload.decode("utf-8", errors="replace")
        with self._lock, self.conn:
            cur = self.conn.execute(
                "INSERT INTO raw_messages(consumer_received_at, topic, payload,"
                " acquisition, source, event_key, status, reason)"
                " VALUES (?,?,?,?,?,?,?,?)",
                (consumer_ts, topic, payload, acquisition, source,
                 event_key, status, reason))
            return cur.lastrowid

    def save_result(self, raw_id, result) -> int:
        """Guarda observações e rejeições. Devolve o nº de observações NOVAS.

        Idempotente: UNIQUE (event_key, quantity) + INSERT OR IGNORE.
        """
        new = 0
        with self._lock, self.conn:
            for o in result.observations:
                cur = self.conn.execute(
                    "INSERT OR IGNORE INTO observations(event_key, device_id,"
                    " quantity, value, unit, quality, received_at, measured_at,"
                    " time_origin, source, acquisition)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (o.event_key, o.device_id, o.quantity, o.value, o.unit,
                     o.quality, o.received_at, o.measured_at, o.time_origin,
                     o.source, o.acquisition))
                new += cur.rowcount
            for i in result.issues:
                self.conn.execute(
                    "INSERT INTO rejections(raw_message_id, quantity, status, reason)"
                    " VALUES (?,?,?,?)",
                    (raw_id, i.quantity, i.status, i.reason))
        return new

    def count(self, table: str) -> int:
        assert table in {"raw_messages", "observations", "rejections"}
        with self._lock:
            return self.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]

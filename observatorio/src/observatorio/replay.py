"""Reprodução de mensagens guardadas (uma por linha, em JSON)."""
import argparse
import logging

from .processing import process_message
from .storage import Store


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ficheiro")
    p.add_argument("--db", default="data/ensaio.db")
    p.add_argument("--source", choices=["real", "synthetic"], default="real")
    a = p.parse_args()
    logging.basicConfig(level=logging.WARNING)
    store = Store(a.db)
    with open(a.ficheiro, "rb") as f:
        for line in f:
            if line.strip():
                process_message(store, "replay", line.strip(),
                                acquisition="replay", source=a.source)
    print(f"tentativas={store.count('raw_messages')} "
          f"observacoes_aceites={store.count('observations')} "
          f"rejeicoes={store.count('rejections')}")


if __name__ == "__main__":
    main()

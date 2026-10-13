"""Executar na raiz: python -m gl01_demo dados/ex02_observacao_valida.json."""

import argparse
import json
import sys

from .dominio import criar_resumo
from .io_local import ler_mensagem


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="GL01: lê uma amostra local autorizada e apresenta sete campos."
    )
    parser.add_argument("ficheiro", help="Caminho da amostra JSON de demonstração.")
    args = parser.parse_args(argv)
    try:
        mensagem = ler_mensagem(args.ficheiro)
    except (OSError, UnicodeError, ValueError):
        print("ERRO: ficheiro ilegível, JSON inválido ou raiz diferente de objeto.",
              file=sys.stderr)
        return 2
    try:
        resumo = criar_resumo(mensagem)
    except KeyError:
        print("ERRO: a amostra não contém todos os campos exigidos pelo GL01.",
              file=sys.stderr)
        return 2
    print(json.dumps(resumo, ensure_ascii=False, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

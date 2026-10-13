"""Verificação local de leitura; sem IP, utilizador, caminhos ou secrets."""

import json
import platform
import sys


def main():
    compativel = sys.version_info >= (3, 11)
    virtual = sys.prefix != sys.base_prefix
    print(json.dumps({
        "python": platform.python_version(),
        "sistema": platform.system(),
        "arquitetura": platform.machine(),
        "ambiente_virtual": virtual,
        "python_minimo_gl01": "3.11",
        "versao_compativel_gl01": compativel,
        "validacao_fisica_bancada": "nao_realizada_por_esta_ferramenta"
    }, ensure_ascii=False, indent=2))
    return 0 if compativel and virtual else 2


if __name__ == "__main__":
    raise SystemExit(main())

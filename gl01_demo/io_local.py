"""Leitura local de JSON. Código de apoio fornecido, não tarefa de GL01."""

import json
from pathlib import Path


def ler_mensagem(caminho):
    """Lê um objeto JSON de um ficheiro UTF-8 autorizado, sem o alterar.

    Verifica apenas que o documento é um objeto. Não valida as regras
    semânticas do contrato MT01 nem descodifica uma mensagem LoRaWAN.
    """
    with Path(caminho).open(encoding="utf-8") as ficheiro:
        mensagem = json.load(ficheiro)
    if not isinstance(mensagem, dict):
        raise ValueError("A raiz do documento deve ser um objeto JSON.")
    return mensagem

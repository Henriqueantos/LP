"""Tarefa GL01. A falha inicial abaixo é deliberada e deve ser completada."""

from pathlib import Path
import unittest

from gl01_demo.dominio import criar_resumo
from gl01_demo.io_local import ler_mensagem

DADOS = Path(__file__).resolve().parents[1] / "dados"


class TestPrimeiroTeste(unittest.TestCase):
    def test_preserva_zero(self):
        entrada = ler_mensagem(DADOS / "ex02_observacao_valida.json")
        saida = criar_resumo(entrada)
        # Substituir self.fail por asserções baseadas em CA-GL01-01.
        # Escrever o resultado esperado a partir do contrato, não do programa.
        self.fail("Tarefa GL01 por concluir: verificar zero e qualidade.")

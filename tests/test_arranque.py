"""Dois testes fornecidos: confirmam o acesso às amostras, não a tarefa."""

from pathlib import Path
import unittest

from gl01_demo.io_local import ler_mensagem

DADOS = Path(__file__).resolve().parents[1] / "dados"


class TestArranque(unittest.TestCase):
    def test_amostra_e_sintetica(self):
        mensagem = ler_mensagem(DADOS / "ex02_observacao_valida.json")
        self.assertEqual(mensagem["source_kind"], "synthetic")
        self.assertEqual(mensagem["acquisition_mode"], "replay")

    def test_amostra_de_ausencia(self):
        mensagem = ler_mensagem(DADOS / "ex02_observacao_ausente.json")
        self.assertIsNone(mensagem["value"])
        self.assertEqual(mensagem["quality"], "missing")

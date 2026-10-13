"""Projeção de uma amostra de demonstração já conhecida.

Não valida o contrato completo, não normaliza mensagens do sensor e não
implementa idempotência. Estes aspetos serão desenvolvidos posteriormente.
"""


def criar_resumo(mensagem):
    """Seleciona sete campos para apresentação, sem alterar a entrada.

    Pré-condição: dicionário plano de uma das amostras autorizadas do GL01,
    com todos os campos abaixo e valores já conformes ao contrato MT01.
    Preserva zero, None, qualidade e proveniência. Não converte unidades,
    não consulta a rede e não cria marcas temporais. Uma chave ausente
    origina KeyError; a validação de dados arbitrários está fora do âmbito.
    A projeção não substitui a observação integral, conservada no ficheiro.
    """
    return {
        "device_id": mensagem["device_id"],
        "quantity": mensagem["quantity"],
        "value": mensagem["value"],
        "unit": mensagem["unit"],
        "quality": mensagem["quality"],
        "source_kind": mensagem["source_kind"],
        "acquisition_mode": mensagem["acquisition_mode"],
    }

# Contrato parcial de utilização — GL01
## Origem e delimitação
Base: contrato MT01/EX02 e MP01 (R01/R02/R03/R05/R12). As escolhas de função,
ficheiros, tarefas e critérios CA-GL01 são a operacionalização deste guião.
Este exercício NÃO redefine o contrato do projeto e NÃO constitui M1.

## Função fornecida: criar_resumo(mensagem)
Pré-condição: um dos objetos planos dos dois JSON autorizados em `dados/`.
A função devolve um novo dicionário com device_id, quantity, value, unit,
quality, source_kind e acquisition_mode, com os valores recebidos.
Não altera a entrada. Não valida tipos, qualidade, identificadores, tempos ou
proveniência. Não converte valores. Não recebe dados de equipamento nem
implementa deduplicação. As amostras integrais conservam os restantes campos.

## Critérios de aceitação da demonstração
**CA-GL01-01:** Dada a amostra ex02_observacao_valida.json, quando criar_resumo
é executada, a saída contém value=0 e quality='valid'. Origem e modo continuam
synthetic/replay. Zero não é substituído por None.
**CA-GL01-02:** Dada a amostra ex02_observacao_ausente.json, a apresentação
contém value=null e quality='missing'. Em Python, a ausência corresponde a None.
**CA-GL01-03:** A execução e os testes não alteram os ficheiros de origem.

A tarefa obrigatória de teste cobre o par value/quality de CA-GL01-01. Os outros
campos são confirmados na execução orientada. Uma extensão pode automatizar
CA-GL01-02 ou a não alteração do objeto, sem nova ponderação de avaliação.

## Falha intencional
O ficheiro tests/test_primeiro_teste.py contém self.fail: é uma tarefa por
concluir, não um erro de instalação. Os dois testes de arranque passam sem
resolver a tarefa. Depois de completar a asserção, há três testes aprovados.

## Alteração controlada
Depois de o teste passar, substituir temporariamente, em dominio.py,
`"value": mensagem["value"],` por `"value": mensagem["value"] or None,`.
O teste deverá detetar a alteração. Restaurar a expressão correta e repetir.
Não alterar a expectativa para fazer aprovar uma implementação errada.
Este exercício é uma verificação de sensibilidade de um teste; não constitui
um processo completo de desenvolvimento orientado por testes.

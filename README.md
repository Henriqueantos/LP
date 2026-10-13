# GL01: Preparação do ambiente e primeira execução

## Percurso rápido (Linux/Pi preparado)
Copiar apenas esta pasta para uma pasta de trabalho nova (por exemplo ~/lp/gl01).
Executar os comandos na raiz, onde este README se encontra:
```bash
python3 -m venv .venv
./.venv/bin/python ferramentas/verificar_ambiente.py
./.venv/bin/python -m gl01_demo dados/ex02_observacao_valida.json
./.venv/bin/python -m unittest tests.test_arranque -v
```
Consultar AMBIENTE.md para Windows e condições de contingência. Sem dependências
externas; não há qualquer comando pip install.

## Tarefa obrigatória
1. Ler CONTRATO_GL01.md; prever os resultados antes de executar.
2. Criar o repositório e registar a base fornecida conforme o guião.
3. Preencher docs/arquitetura_inicial.md e docs/evidencias_gl01.md (ou ficha Word).
4. Completar tests/test_primeiro_teste.py: substituir self.fail pelas asserções
   para value=0 e quality='valid'. Não alterar a amostra nem copiar o resultado
   da implementação como valor esperado.
5. Executar:
```bash
./.venv/bin/python -m unittest tests.test_primeiro_teste -v
./.venv/bin/python -m unittest discover -s tests -v
```
6. Testar a alteração controlada em dominio.py indicada no contrato, observar a
   falha e restaurar. O conjunto final deverá aprovar os três testes obrigatórios.
7. Rever alterações e registar o commit final; comunicar o identificador ao docente.

## Estados esperados
- Antes da tarefa: CLI executa; dois testes de arranque aprovados.
- O conjunto completo inicialmente falha em UM teste (self.fail deliberado).
- Depois da tarefa: três testes aprovados.
- Durante a alteração controlada: o teste do zero falha.
- Depois da reposição: três testes aprovados; ficheiros de origem inalterados.
Testes adicionais podem aumentar a contagem; documentar o que foi acrescentado.

## Organização
- gl01_demo/: código de demonstração fornecido (entrada/saída e função de domínio).
- dados/: duas amostras sintéticas e contrato MT01 de referência.
- tests/: dois testes prontos e um teste explicitamente por concluir.
- docs/: modelos de arquitetura e evidências; não introduzir dados sensíveis.
- ferramentas/: uma verificação local que não valida a bancada física.

Os critérios deste GL01 são formativos e não acrescentam ponderações à FUC.
A configuração do sensor/gateway, TTN, MQTT, Django e Docker não integra esta aula.
Referências e delimitação: REFERENCIAS.md e CONTRATO_GL01.md.

# Requisitos (M1)

| ID | Requisito | Critério de aceitação | Evidência |
|----|-----------|----------------------|-----------|
| RF-01 | Receber uplinks do dispositivo via MQTT | Uma mensagem real chega e é registada | consumer.py, docs/aquisicao.md |
| RF-02 | Distinguir dados válidos, ausentes e inválidos | Teste com os três casos | tests/test_validation.py |
| RF-03 | Ausência nunca é convertida em zero | Campo em falta não gera observação | tests/test_validation.py |
| RF-04 | Rejeição com motivo, sem parar o processamento | Mensagem inválida seguida de válida: a válida é processada | tests/test_processing.py |
| RF-05 | Registar todas as mensagens recebidas | Uma linha em raw_messages por tentativa | tests/test_processing.py |
| RF-06 | Idempotência por evento | Reprocessar 2x não aumenta as observações aceites | tests/test_processing.py, ensaio de replay |
| RF-07 | Preservar unidades e proveniência | Cada observação tem unidade, origem e modo de aquisição | tests/test_validation.py |
| RF-08 | Segredos fora do código | .env ignorado pelo Git; .env.example no repositório | revisão do repositório |

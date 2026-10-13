# EX02: Contrato de demonstração

**Natureza:** exemplo didático original. Não é o payload real do sensor nem o contrato obrigatório dos grupos. Não se afirma que foi validado em hardware.

## Âmbito
Cada objeto representa uma observação de uma grandeza num evento. O exemplo usa apenas `indice_demo`, com unidade fictícia `u_demo`. Uma mensagem real poderá originar várias observações.

- `event_id` e `device_id`: texto não vazio. Na amostra, event_id é estável por evento; não se calcula a partir do valor.
- `quantity` e `unit`: códigos declarados; não inferir do nome comercial do sensor.
- `value`: número finito ou null. Texto e booleanos são inválidos neste exemplo.
- `quality`: `valid` quando existe número finito; `missing` quando value é null. Entrada malformada é rejeitada e registada separadamente, não apresentada como observação válida.
- `measured_at`: instante com fuso conhecido, ou null quando não existe informação. Nas amostras é sempre null.
- `received_at`: instante da primeira receção pelo consumidor, com fuso, conservado na reprodução. O instante de execução da reprodução é registado fora da observação. Esta escolha deve ser revista se o contrato real utilizar outra semântica.
- `source_kind`: `real` ou `synthetic`; identifica a origem dos dados.
- `acquisition_mode`: `live` ou `replay`; identifica o modo de disponibilização. Uma observação real reproduzida continua com source_kind=real.
- `raw_ref`: referência estável à mensagem original, sem segredos.

A identidade de uma observação na amostra é a combinação (device_id, event_id, quantity). O contrato de integração real tem de justificar a identidade do evento e tratar o caso de múltiplas grandezas.

## Ficheiros
- ex02_observacao_valida.json: zero válido, tempos e proveniência explícitos.
- ex02_observacao_ausente.json: ausência declarada, não convertida em zero.
- ex02_mensagem_invalida.json: contraexemplo intencional; o texto `erro` não é um número.
- ex03_sequencia_reproducao.jsonl: eventos demo-001, demo-001 e demo-004. Resultado conceptual: duas observações distintas, ambas com valor zero, para uma única grandeza. As tentativas de receção podem ser três.

**Fonte do requisito:** MP01, R05/R06 e §4.3. Campos, unidades fictícias e amostras: elaboração didática MT01.

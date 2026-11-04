# Contrato de dados (M1) — VERSÃO PROVISÓRIA

> Estado: os campos do sensor ainda NÃO estão confirmados (sem acesso à consola do
> The Things Stack). Os nomes grandeza_a e grandeza_b são marcadores de posição
> e serão substituídos pelos campos reais do HKT IAQ-900 O3 assim que houver uma
> mensagem real. Não se inferem grandezas a partir da designação comercial.

## Campos de cada observação
| Informação | Campo | Regra |
|---|---|---|
| Dispositivo | device_id | Identificador estável do TTS; sem dados pessoais |
| Grandeza | quantity | Apenas campos confirmados |
| Valor | value | Numérico; ausente nunca vira zero |
| Unidade | unit | Definida por grandeza no contrato |
| Qualidade | quality | "ok" se válido |
| Receção | received_at | UTC, ISO 8601, vem do TTS |
| Medição | measured_at | Vazio quando desconhecido (não se inventa) |
| Origem do tempo | time_origin | Ex.: "ttn.received_at" |
| Evento | event_key | dispositivo + sessão + contador de trama (f_cnt) |
| Proveniência | source | "real" ou "synthetic" |
| Modo | acquisition | "live" ou "replay" |

## Chave de evento
event_key = device_id | session_key_id | f_cnt
- O f_cnt reinicia quando há um novo join, por isso inclui-se a sessão.
- Não depende do gateway (a mesma transmissão pode ser recebida por vários).
- Não depende do valor (duas medições iguais não são o mesmo evento).
- Limitação: se o TTS omitir f_cnt quando vale 0, assume-se 0.

## Estados de um campo
- *válido*: presente, numérico e dentro do intervalo
- *ausente*: não veio na mensagem (não gera observação)
- *inválido*: veio mas fora do tipo ou do intervalo (registado com motivo)

## Convenção temporal
UTC, formato ISO 8601. Quando o instante de medição não existe, usa-se o instante
de receção como aproximação, o que é indicado em time_origin e tem como limitação
a latência da rede.

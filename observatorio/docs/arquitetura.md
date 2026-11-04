# Arquitetura (M1)

## Diagrama de contexto
mermaid
flowchart LR
  S[Sensor HKT IAQ-900] -->|LoRaWAN| G[Gateway Dragino]
  G --> T[The Things Stack]
  T -->|MQTT QoS 0| O[Observatório no Raspberry Pi]
  U[Grupo e docente] -->|consulta e testes| O


## Diagrama de componentes
mermaid
flowchart LR
  C[consumer.py<br/>receção MQTT] --> P[processing.py<br/>orquestração]
  P --> V[validation.py<br/>validação e normalização]
  P --> ST[storage.py<br/>persistência]
  R[replay.py<br/>reprodução] --> P


## Responsabilidades
- *consumer.py*: liga ao broker, recebe mensagens e entrega-as ao processamento. Não valida.
- *processing.py*: coordena o fluxo e garante que um erro numa mensagem não pára as seguintes.
- *validation.py*: aplica o contrato de dados e devolve observações válidas e problemas.
- *storage.py*: guarda mensagens, observações e rejeições; garante a idempotência.
- *replay.py*: reprocessa mensagens guardadas, assinalando-as como reprodução.

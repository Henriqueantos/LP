# Ambiente do exercício
Opção didática GL01: Python 3.11 ou posterior autorizado pelo docente; Git com
suporte a `git init -b main` (2.28 ou posterior), editor e módulo venv instalados.
A versão exata e o equipamento usados devem ser registados, não presumidos.
Não há dependências externas, nem `pip install`, Django, Paho ou Docker.
Não reutilizar o ambiente .venv-mp02 da sonda técnica. Criar .venv neste projeto.

## Linux / Raspberry Pi OS / macOS preparado
Na raiz do projeto (onde estão README.md, gl01_demo e tests):
```bash
python3 --version
git --version
python3 -m venv .venv
./.venv/bin/python ferramentas/verificar_ambiente.py
./.venv/bin/python -m gl01_demo dados/ex02_observacao_valida.json
./.venv/bin/python -m unittest tests.test_arranque -v
```
## Windows preparado (PowerShell)
Apenas se autorizado como alternativa local; Python e Git já instalados:
```powershell
py -3 --version
git --version
py -3 -m venv .venv
.\.venv\Scripts\python.exe ferramentas/verificar_ambiente.py
.\.venv\Scripts\python.exe -m gl01_demo dados/ex02_observacao_valida.json
.\.venv\Scripts\python.exe -m unittest tests.test_arranque -v
```
Nos restantes comandos do guião, substituir `./.venv/bin/python` por
`.\.venv\Scripts\python.exe`. Não se ativa o ambiente por script: não é
necessário alterar a política PowerShell. Se `py` não existir, usar apenas o
intérprete indicado pelo docente. Não instalar software durante a tarefa.

O acesso SSH real ao Pi segue MP02/P01 e exige endereço, conta e impressão
digital confirmados pelo docente. A ausência do Pi não impede o percurso local;
registar a contingência e manter a verificação física como não observada.
Se a criação de venv falhar, não usar sudo pip nem contornar a gestão de pacotes.
O docente corrige o aprovisionamento ou indica outra máquina preparada.

Não copiar .venv entre máquinas: recriar a partir de um intérprete autorizado.
Os exemplos podem executar sem rede depois de os materiais serem distribuídos.

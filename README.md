# Google Automation Labs

Este repositório reúne exemplos de automação em Python e um notebook de demonstração para uso com VS Code + Colab.

Para o proposito do curso do Google, voce tambem pode usar o Colab Web: https://colab.research.google.com.

No Colab Web, a opcao **Mostrar terminal** no menu **Comandos** abre o mesmo ambiente de shell do notebook, onde voce pode executar comandos Linux.

## Estado atual do notebook demo

- A análise mais recente está em `demo.md`.
- Situação resumida do `demo.ipynb`:
	- Convenção de idioma: aprovado.
	- `.venv` no `.gitignore`: aprovado.
	- `requirements.txt`: aprovado.
	- Caminhos absolutos: atenção por uso didático de `/etc/os-release`.

## Estrutura principal

- `demo.ipynb`: notebook de demonstração (Colab).
- `demo.md`: anotações/avaliação do notebook.
- `hello_world.py`: script simples de exemplo.
- `system_health_check.py`: script de verificação básica de saúde de diretório/disco.
- `requirements.txt`: dependências Python do projeto.
- `setup.ps1`: preparação do ambiente Python no Windows (PowerShell).
- `setup_and_edit.sh`: preparação de editor e edição de arquivo em Linux (bash + apt).

## Scripts de setup: onde, quando e para que usar

| Script | Onde executar | Quando executar | Para que serve |
|---|---|---|---|
| `setup.ps1` | Windows PowerShell, na raiz do projeto | Na primeira configuração local no Windows, ou quando quiser reinstalar dependências da `requirements.txt` | Cria `.venv` (se não existir) e instala dependências Python com `pip` |
| `setup_and_edit.sh` | Linux/WSL com `bash` e `apt`, como root (`sudo`) | Quando precisar garantir que o editor `nano` esteja instalado e abrir rapidamente `hello_world.py` no terminal | Instala `nano` (se faltar), lista os arquivos da pasta e abre `hello_world.py` no `nano` |

### 1) setup.ps1 (Windows)

Use este script para preparar o ambiente Python local no Windows.

Comando (PowerShell):

```powershell
./setup.ps1
```

O que ele faz:
1. Verifica se a pasta `.venv` existe.
2. Cria o ambiente virtual se necessário.
3. Instala as dependências de `requirements.txt` usando o `pip` da própria `.venv`.

## 2) setup_and_edit.sh (Linux/WSL)

Use este script em sistemas Linux (ou WSL) quando quiser praticar edição de arquivos no terminal com `nano`, dentro da proposta pedagógica do curso.

Comando:

```bash
sudo ./setup_and_edit.sh
```

O que ele faz:
1. Exige execução como root (checagem de `id -u`).
2. Instala `nano` com `apt` se o editor não estiver disponível.
3. Executa `ls -l` na pasta atual.
4. Abre `hello_world.py` no `nano`.

Contexto de aprendizado:
- O uso do `nano` aqui é intencional para prática durante o curso **Using Python to Interact with the Operating System - Google** (Coursera: https://www.coursera.org/learn/python-operating-system).

## Upload to Colab: quais arquivos enviar

No `demo.ipynb`, os arquivos locais que devem ser enviados são:

- **Obrigatório:** `hello_world.py` (teste de integração Colab no VS Code).
- **Obrigatório:** `MCMV.png` (célula de imagem local).

Sem `MCMV.png`, a célula informa que o arquivo não foi encontrado e não exibe a imagem local.

Arquivos opcionais no contexto do notebook:

- `requirements.txt`: útil como referência de dependências do projeto (embora o Colab já traga vários pacotes pré-instalados).
- `system_health_check.py`: opcional no Colab; a execução principal dele é no VS Code local.

### Como fazer Upload to Colab no VS Code

Referencias oficiais da extensao:
- Repositorio no GitHub: https://github.com/googlecolab/colab-vscode
- User Guide: https://github.com/googlecolab/colab-vscode/wiki/User-Guide

1. No Explorer do VS Code, clique com o botão direito no arquivo local.
2. Selecione **Upload to Colab**.
3. Confirme no painel do Colab (`COLAB: CONTENTS`) se o arquivo apareceu.
4. Execute a célula correspondente no `demo.ipynb`.

## Fluxo recomendado

1. **Windows local:** execute `setup.ps1` para preparar a `.venv`.
2. **VS Code local (validação do ambiente):** execute `system_health_check.py` para verificar uso de disco e listar arquivos grandes da pasta atual.
3. **Notebook no Colab:** abra `demo.ipynb` e faça Upload to Colab de `hello_world.py` (teste Colab no VS Code) e `MCMV.png` (imagem local).
4. **Linux/WSL (opcional e pedagógico):** use `setup_and_edit.sh` para praticar edição via terminal com `nano`, como parte do curso.

## Checklist pre-commit do lab (Copilot Chat)

Use o prompt versionado em `.github/prompts/lab-precommit-checklist.prompt.md` para validar o notebook antes de commit e push.

Como rodar no Copilot Chat (Agent):
1. Abra o Copilot Chat no VS Code.
2. Execute `/lab-precommit-checklist demo.ipynb`.
3. Revise o resultado e atualize `demo.md` com o status final.

Critérios checados pelo prompt:
- Convenção de idioma (identificadores/comentários em inglês; mensagens ao usuário podem ficar em PT-BR).
- Caminhos absolutos hardcoded.
- Entradas essenciais no `.gitignore` (`.venv/`, `__pycache__/`, `*.pyc`).
- Dependências externas refletidas em `requirements.txt`.

Antes do commit final:
1. Decida se as saídas do `demo.ipynb` devem permanecer versionadas.
2. Trate ou justifique explicitamente o uso de `/etc/os-release` no contexto didático.

# Google Automation Labs

Repositório de exemplos práticos de Python multiplataforma, criado para acompanhar o curso **Using Python to Interact with the Operating System** (Google/Coursera).

O material foi desenvolvido para rodar tanto no **Google Colab** (via extensão do VS Code ou pelo Colab Web) quanto em ambientes locais **Windows** e **Linux/WSL**.

---

## Notebooks

### `demo.ipynb`

Guia demonstrativo de desenvolvimento multiplataforma. Cobre:

1. **Autenticação no Colab** — autenticação OAuth via `google.colab.auth`, com exibição da conta autenticada.
2. **Exploração do ambiente Linux** — versão do kernel e distribuição via módulo `platform`.
3. **Manipulação de caminhos e arquivos** — criação de estrutura de diretórios com `os.makedirs` e `pathlib`.
4. **Comandos de sistema multiplataforma** — comparação entre Python puro, Linux (`pwd`, `ls`) e Windows (`cd`, `dir`).
5. **Informações do SO** — `platform` (universal), `lsb_release` (Linux) e `ver` (Windows).
6. **Gerenciamento de pacotes** — `pip` (universal) vs. `apt-get` (Linux/Colab).
7. **Transferência de arquivos VS Code ↔ Colab** — upload e download pela extensão Colab.
8. **Exibição de imagens** — arquivo local (`Pillow` + `pathlib`) e download via URL (`urllib`).
9. **Verificação do `pip`** — via `subprocess` e `sys.executable`, cross-platform.
10. **DataFrames com pandas** — criação e exibição de tabelas com `pd.DataFrame`.

### `Terminal_Linux.ipynb`

Notebook dedicado ao uso do terminal Linux no Colab. Inclui guia de persistência de `virtualenv` entre sessões.

---

## Scripts

| Arquivo | Onde executar | Para que serve |
|---|---|---|
| `setup.ps1` | Windows PowerShell, na raiz do projeto | Cria `.venv` (se não existir) e instala dependências de `requirements.txt` |
| `setup_and_edit.sh` | Linux/WSL com `bash` e `apt`, como root | Instala `nano`, lista arquivos e abre `hello_world.py` no editor |
| `hello_world.py` | Qualquer ambiente | Script de exemplo com tratamento de erros de I/O (`OSError`) |
| `system_health_check.py` | VS Code local | Verificação básica de saúde de diretório e uso de disco |

### `setup.ps1` (Windows)

```powershell
./setup.ps1
```

1. Verifica se `.venv` existe.
2. Cria o ambiente virtual se necessário.
3. Instala as dependências de `requirements.txt` com o `pip` da própria `.venv`.

### `setup_and_edit.sh` (Linux/WSL)

```bash
sudo ./setup_and_edit.sh
```

1. Exige execução como root.
2. Instala `nano` via `apt` se não estiver disponível.
3. Executa `ls -l` na pasta atual.
4. Abre `hello_world.py` no `nano`.

> O uso do `nano` é intencional para prática de edição via terminal, conforme proposta pedagógica do curso.

---

## Colab Web

Para usar sem o VS Code, acesse [colab.research.google.com](https://colab.research.google.com), abra `Terminal_Linux.ipynb` e acesse o terminal pelo menu **Comandos > Mostrar terminal**.

---

## Upload to Colab (VS Code)

Antes de executar as células de imagem local e integração no `demo.ipynb`, envie os arquivos necessários:

| Arquivo | Obrigatório | Célula correspondente |
|---|---|---|
| `hello_world.py` | Sim | Teste de integração Colab no VS Code |
| `MCMV.png` | Sim | Exibição de imagem local |
| `requirements.txt` | Não | Referência de dependências |

Como enviar:

1. No Explorer do VS Code, clique com o botão direito no arquivo.
2. Selecione **Upload to Colab**.
3. Confirme no painel `COLAB: CONTENTS` que o arquivo apareceu.
4. Execute a célula correspondente no `demo.ipynb`.

Referências da extensão: [GitHub](https://github.com/googlecolab/colab-vscode) · [User Guide](https://github.com/googlecolab/colab-vscode/wiki/User-Guide)

---

## Fluxo recomendado

1. **Windows local:** execute `setup.ps1` para preparar a `.venv`.
2. **Validação local:** execute `system_health_check.py` no VS Code para verificar o ambiente.
3. **Colab:** abra `demo.ipynb`, faça upload de `hello_world.py` e `MCMV.png` e execute as células em ordem.
4. **Linux/WSL (opcional):** use `setup_and_edit.sh` para praticar edição no terminal com `nano`.

---

## Checklist pré-commit

Use o prompt em `.github/prompts/lab-precommit-checklist.prompt.md` para validar o notebook antes de commit.

No Copilot Chat (Agent mode):

```
/lab-precommit-checklist demo.ipynb
```

Critérios verificados:

- Convenção de idioma: identificadores e comentários em inglês; mensagens ao usuário podem ficar em PT-BR.
- Caminhos absolutos hardcoded.
- Entradas essenciais no `.gitignore` (`.venv/`, `__pycache__/`, `*.pyc`).
- Dependências externas refletidas em `requirements.txt`.

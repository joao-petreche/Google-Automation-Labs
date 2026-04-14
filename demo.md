# Analise do notebook demo.ipynb

Checklist executado para `demo.ipynb`.

## Resumo

| # | Item | Status |
|---|---|---|
| 1 | Convencao de idioma | Reprovado |
| 2 | Sem caminhos absolutos | Reprovado |
| 3 | `.venv` no `.gitignore` | Aprovado |
| 4 | `requirements.txt` atualizado | Reprovado |

## 1. Convencao de idioma

Status: Reprovado

O notebook mistura comentarios e mensagens inline em portugues dentro de celulas de codigo, o que foge da regra do Mentor para manter o codigo em ingles.

Ocorrencias principais:
- Celula 8: comentario em portugues sobre o diretorio de trabalho do Colab.
- Celula 10: comentarios em portugues sobre `gcloud`.
- Celula 12: comentario em portugues sobre `lsb_release`.
- Celula 14: comentarios em portugues sobre `apt`.
- Celula 16: comentarios e mensagens ao usuario em portugues dentro da celula de codigo.

Correcao sugerida:
- Manter explicacoes em PT-BR nas celulas Markdown.
- Traduzir comentarios de codigo para ingles.
- Manter mensagens ao usuario em PT-BR apenas se isso for intencional e fizer parte da interface do notebook.

## 2. Caminhos absolutos

Status: Reprovado

Ha caminhos absolutos hardcoded no notebook.

Ocorrencias principais:
- Celula 4: leitura de `/etc/os-release` via `subprocess`.
- Celula 16: `image_path = '/content/MCMV.png'`.
- Celula 16: comando `!ls -la /content/MCMV.png`.

Correcao sugerida:
- Para arquivos do projeto, preferir `pathlib.Path`, `os.path.join()` ou caminhos relativos.
- Para caminhos de sistema inevitaveis, encapsular o valor em uma variavel nomeada e validar existencia antes de usar.

Exemplo:

```python
from pathlib import Path

image_path = Path("MCMV.png")
if image_path.exists():
    img = Image.open(image_path)
```

## 3. .venv no .gitignore

Status: Aprovado

O `.gitignore` do projeto contem as entradas essenciais:
- `.venv/`
- `__pycache__/`
- `*.pyc`

## 4. requirements.txt atualizado

Status: Reprovado

O notebook usa bibliotecas externas e o projeto nao possui `requirements.txt`.

Dependencias externas identificadas:
- Celula 16: `from PIL import Image`
- Celula 16: `from IPython.display import display`
- Celula 21: `import pandas as pd`

Conteudo sugerido para `requirements.txt`:

```txt
Pillow
ipython
pandas
```

Observacao:
No Colab, algumas dessas bibliotecas podem ja estar instaladas, mas o repositorio deve documenta-las para manter a reprodutibilidade fora do ambiente hospedado.

## Conclusao

O notebook ainda nao esta pronto para commit segundo o checklist do Mentor.

Correcoes pendentes:
1. Traduzir comentarios de codigo para ingles.
2. Remover ou encapsular caminhos absolutos hardcoded.
3. Criar `requirements.txt` com as dependencias externas usadas no notebook.

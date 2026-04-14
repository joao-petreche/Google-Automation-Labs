# Analise do notebook demo.ipynb

Checklist executado para `demo.ipynb` com base no estado atual do workspace.

## Resumo

| # | Item | Status |
|---|---|---|
| 1 | Convencao de idioma | Reprovado |
| 2 | Caminhos do projeto sem hardcode | Aprovado com ressalva |
| 3 | `.venv` no `.gitignore` | Aprovado |
| 4 | `requirements.txt` atualizado | Aprovado |
| 5 | Celulas com efeitos externos identificadas | Atencao |
| 6 | Notebook com saidas de execucao | Atencao |

## 1. Convencao de idioma

Status: Reprovado

Pelas regras do Mentor, explicacoes podem ficar em PT-BR, mas codigo, identificadores, comentarios e mensagens emitidas por celulas de codigo devem preferencialmente ficar em ingles.

No estado atual, o notebook ainda mistura ingles e portugues dentro de celulas de codigo.

Ocorrencias principais:
- Celula 2: mensagens de `print` em portugues.
- Celula 8: mensagem exibida ao usuario em portugues.
- Outras celulas de codigo ja foram parcialmente ajustadas e estao melhores do que na versao anterior.

Correcao sugerida:
- Manter o texto pedagogico em PT-BR nas celulas Markdown.
- Traduzir mensagens e comentarios das celulas de codigo para ingles.

## 2. Caminhos do projeto sem hardcode

Status: Aprovado com ressalva

O problema anterior com caminho absoluto do arquivo de imagem foi corrigido.

Estado atual:
- A celula de imagem usa `Path("MCMV.png")`, o que e adequado para um arquivo do projeto.
- Nao ha mais uso de `'/content/MCMV.png'` como caminho hardcoded do arquivo da imagem.

Ressalva:
- A leitura de `/etc/os-release` continua aparecendo em uma celula, mas isso e aceitavel neste notebook porque se trata de um caminho padrao de sistema Linux usado apenas para inspecao do ambiente.
- As referencias a `/content` tambem sao coerentes com o contexto de Google Colab e nao configuram problema de caminho de arquivo do projeto.

## 3. .venv no .gitignore

Status: Aprovado

O `.gitignore` do projeto contem as entradas essenciais:
- `.venv/`
- `__pycache__/`
- `*.pyc`

## 4. requirements.txt atualizado

Status: Aprovado

O projeto possui `requirements.txt` e ele cobre as dependencias externas identificadas no notebook.

Dependencias encontradas no notebook:
- `from PIL import Image`
- `from IPython.display import display`
- `import pandas as pd`

Dependencias registradas em `requirements.txt`:

```txt
Pillow
ipython
pandas
```

## 5. Celulas com efeitos externos identificadas

Status: Atencao

O notebook contem celulas que dependem de ambiente externo, rede, autenticacao ou privilegios elevados.

Ocorrencias principais:
- Celula 10: `gcloud config get-value account`
- Celula 14: `sudo apt update` e `sudo apt install python3-pil -y`
- Celula 18: `wget` para baixar imagem por URL

Isso nao impede commit, mas reduz a reprodutibilidade imediata fora do Colab ou sem configuracao previa.

## 6. Notebook com saidas de execucao

Status: Atencao

O notebook esta salvo com `outputs` e `execution_count` em varias celulas.

Isso pode ser intencional para demonstracao, mas vale decidir antes do commit:
- manter as saidas para preservar o contexto do demo;
- ou limpar os outputs para reduzir ruido no diff do repositorio.

## Conclusao

O notebook esta bem mais proximo de ficar pronto para commit do que a avaliacao anterior indicava.

Pendencias reais no estado atual:
1. Ajustar a convencao de idioma nas celulas de codigo.
2. Decidir se as saidas do notebook devem permanecer versionadas.
3. Manter consciencia de que algumas celulas dependem de Colab, rede, `gcloud` e `apt`.

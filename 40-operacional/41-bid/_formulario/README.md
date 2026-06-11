# `_formulario/` — fonte única de respostas + gerador

Recria o formulário do Good Grants com as nossas respostas, valida limites e compara com o OU2. O formulário real é preenchido **pela OU na plataforma** — este kit garante que, quando as respostas fecharem, a transcrição seja copiar-e-colar sem surpresa de limite ou inconsistência.

## Fluxo

1. Resposta fechou? **Edite `respostas.md`** (texto EN no corpo do campo; mude `status:` para `pronto`).
2. Rode `python gerar.py`.
3. Confira o terminal (excessos de limite, `TBD`s, divergências com o OU2) e o `formulario-preenchido.md` gerado.

## Arquivos

| Arquivo | Papel |
|---|---|
| `respostas.md` | **Fonte única.** Um bloco por campo: `## id \| Pergunta`, metadados (`secao`, `limite`, `status`, `ou2`, `nota`), corpo = resposta EN |
| `gerar.py` | Gera o formulário, valida palavras, conta `TBD`, compara com `_versao-ou/…OU2.md` |
| `formulario-preenchido.md` | **Gerado — não editar.** O formulário recriado, com status e contagens por campo |

## Status possíveis

- `pronto` ✅ — validado pelo autor da seção
- `rascunho` 🟨 — texto existe, falta validação humana
- `usar-ou2` 📥 — a resposta vale a do OU2; o script a importa na geração
- `vazio` 🔴 — sem resposta; a `nota:` diz o que destrava (IDs do catálogo)

## Comparação com o OU2

Campos com âncora `ou2:` são localizados no formulário OU2 e comparados: **igual** · **DIFERENTE** (substituir lá pela nossa versão) · **vazio no OU2** (nossa resposta é nova). É a checagem de drift entre o que circulou com a OU e a fonte canônica daqui.

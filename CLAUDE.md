# CLAUDE.md — orientação para a LLM no vault `cefor-ou-tne`

Este repositório é o **segundo cérebro** do projeto TNE Exploratory Grant 2026 (CEFOR/IFES + IET/Open University). Desenho completo em [`cefor-ou-tne-workspace-spec.md`](cefor-ou-tne-workspace-spec.md). Roteamento das camadas e fase ativa em [`CONTEXT.md`](CONTEXT.md).

## O que é

Híbrido consciente: as camadas de conhecimento (`/00`–`/30`, `/50`) seguem o framework Zettelkasten (navegação por links, voz própria assinada); a camada operacional (`/40`) é ICM (top-down, contexto e tracking). O time pensa nas camadas de conhecimento; a candidatura e a execução rodam em `/40`.

## Idioma

- **Vault em português.** As camadas de conhecimento são instrumento de pensamento do time CEFOR — voz própria, em PT.
- **Artefatos que circulam com a OU em inglês.** Concept note e seções do formulário nascem em EN dentro de `/40`. Resumos `-pt.md` quando precisar validar no CEFOR.

## Papel da LLM (seção 6 da spec)

O que **instala conhecimento** é humano; o que é **produção operacional** a LLM acelera.

| Faz | Não faz (humano decide/escreve) |
|---|---|
| Rascunhar textos da candidatura em `/40` a partir do MOC e das Permanent Notes | Decidir o que extrair das fontes |
| Verificar constraints (limite de palavras, EDI, escopo exploratory) | Escrever Permanent Notes e MOCs (pode sugerir conexões) |
| Traduzir/gerar resumos `-pt.md` e versões EN | — |
| Atualizar `_memoria` e `_pontos-a-definir` após sessões (autor confere) | — |

Toda saída da LLM em `/40` exige **revisão do autor da seção** antes de circular.

## Convenções de commit

- Mensagens em português, no imperativo, descritivas. Escopo por camada quando ajudar (ex.: `10.1: extrai marco MEC via Docling`, `41-bid: rascunho do concept note EN`).
- **Sem segredos** (D8). `.env`, credenciais e `.obsidian/` ficam fora — ver `.gitignore`.
- Commits pequenos por unidade de trabalho. Ao fim de cada sessão, atualizar `_memoria` e o catálogo.

## Multi-autor (D4)

Permanent Notes e MOCs têm campo `author` no frontmatter (`vanessa`, `elton`, `marquito`). A voz da nota é de quem assina. Discordância **não** se resolve editando a nota do outro — escreve-se outra nota e linka-se a tensão. MOC pode ser co-autorado: é o estado do entendimento do **time**.

## Ponte conhecimento → candidatura (D7)

Cada seção do formulário em `/40/41-bid/` referencia por wikilink as Permanent Notes (`/20`) e o MOC (`/30a`) que a embasam. Rastreabilidade: "de onde vem essa afirmação?" deve estar a um link de distância.

## Status rápido

`/status-cefor-ou-tne` (slash command em `.claude/commands/`) injeta `_memoria` + `_pontos-a-definir`.

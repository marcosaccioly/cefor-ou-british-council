# Integração do material do Elton — fila de revisão

**Data:** 2026-06-11 · **Quem dispersou:** Marquito (LLM executou o movimento)
**Origem:** merge de `vertumno/cefor-ou-british-council` (upstream) no fork. O Elton mantinha uma versão paralela do projeto, com a mesma filosofia atômica (frontmatter, `[[id]]`), organizada por função (`context/`, `application/`) em vez das camadas do vault.

O material foi **reposicionado nas camadas** (estratégia "mapear direto"). Os movimentos usaram `git mv` — o histórico do Elton está preservado. Este doc é a **fila do que ainda precisa de olhar humano**: o reposicionamento é operacional; a curadoria de conhecimento (D4, seção 6 da spec) é de vocês.

## Onde cada coisa foi parar

| Origem (repo Elton) | Destino no vault |
|---|---|
| `application/00-application-form.md` | `40-operacional/41-bid/00-application-form.md` |
| `application/01-concept-note.md` | `41-bid/01-concept-note/concept-note.md` |
| `application/02-activities-and-mande.md` | `41-bid/04-activities-monitoring/` |
| `application/03-gender-edi-statement.md` | `41-bid/06-gender-edi/` |
| `application/04-budget-worksheet.md` · `05-risks.md` | `41-bid/07-budget-risks-ethics/` |
| `application/06-sustainability-pathway.md` | `41-bid/05-results-sustainability/` |
| `application/README.md` | `41-bid/_guia-redacao-elton.md` |
| `application/assets/*` (CVs, cartas) | `41-bid/08-supporting-docs/` |
| `application/_tracker/*` | `41-bid/_tracker/` |
| `…OU2*.md/docx/PT` (raiz) | `41-bid/_versao-ou/` |
| `tne-briefing-v4.html` · `analise-proposta.html` | `10-literatura/10.1-documentos/` |
| `context/grant/*` + README/INDEX/sources | `10.1-documentos/grant-notes/` |
| `context/brazil/*` | `10-literatura/10.2-conceitos/` |
| `context/partners/*` | `40-operacional/_config/partners/` |
| `context/intelligence/*` | `20-permanent-notes/` (com `author: elton`) |
| `context/proposal/{recommended,path,open-questions}` | `30-sintese/30a-map-of-content/` (com `author: elton`) |

## Pendências de revisão humana

- [ ] **Consolidar `_config` (há duas versões).** O seu `_config/team.md`, `_config/deadlines.md` e `_config/constraints/*` continuam intactos. As versões mais ricas do Elton estão em: `_config/partners/team.md` (vs seu `team.md`), `grant-notes/timeline.md` (vs `deadlines.md`), `grant-notes/{eligibility,assessment-criteria,budget-and-costs}.md` (vs `constraints/*`). Decidir o que funde e o que arquiva — **nada foi sobrescrito**.
- [ ] **Dar voz às notas importadas.** `20-permanent-notes/{winning-patterns,blind-spots}.md` e `30a-map-of-content/{recommended-direction,path-options,open-questions}.md` entraram com `author: elton` e marca `imported`. Pela D4, viram Permanent Note/MOC legítimos só após revisão de quem assina (Elton) ou co-autoria do time no MOC.
- [ ] **Migrar `open-questions-and-next-steps.md`** → itens do catálogo `_pontos-a-definir-cefor-ou-tne.md` (IDs estáveis). Cruzar com as 3 perguntas ao British Council.
- [ ] **Consolidar trackers (D5).** O `41-bid/_tracker/` do Elton (decision-log, submission-checklist, working-log) é redundante com os docs vivos (`_memoria`, `_pontos-a-definir`, `_planejamento`). Migrar o conteúdo e aposentar a pasta.
- [ ] **Seção b (`41-bid/03-tne-core/`) ficou sem draft direto** — o Elton não tinha um arquivo "tne-core". O insumo está espalhado em `grant-notes/tne-strategy.md` + `10.2-conceitos/regulatory-recognition.md` + `01-concept-note/concept-note.md`. É a seção de maior peso (35%): merece o MOC.
- [ ] **Wikilinks `[[id]]`.** Os `id` no frontmatter não mudaram, então os `[[id]]` continuam resolvendo por id. Mas a navegação por pasta mudou; conferir se algum link assumia caminho relativo.

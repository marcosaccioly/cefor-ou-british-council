# Base de Conhecimento — TNE Exploratory Grant 2026 · CEFOR/IFES × Open University

Base de contexto **componentizada** para a candidatura conjunta CEFOR/IFES (Brasil) + Open University (Reino Unido) ao **TNE Exploratory Grants 2026** do British Council.

Cada arquivo é **atômico** (um tópico), carrega **frontmatter** com metadados e **referencia outros componentes** via `[[id]]`. O objetivo é permitir carregamento seletivo de contexto — por um humano ou por um agente — sem precisar reler o briefing inteiro.

---

## Como usar

- **Visão executiva rápida:** leia `../tne-briefing-v4.html` (documento de apresentação).
- **Para escrever a proposta:** comece por [[proposal-recommended-direction]] e [[grant-assessment-criteria]].
- **Para checar um fato específico:** use o [[index]] (mapa de todos os componentes) e abra o arquivo do tópico.
- **Para um agente de IA:** carregue `INDEX.md` primeiro; depois puxe apenas os componentes cujo `id` aparece em `related` do tópico em foco.

## Ordem de carregamento sugerida (para um agente)

1. `INDEX.md` — mapa e metadados de tudo
2. `grant/*` — as regras do jogo (edital)
3. `proposal/recommended-direction.md` — a tese
4. Componentes específicos conforme a tarefa (perfis, regulatório, inteligência)

---

## Convenções

### Frontmatter (schema)

```yaml
---
id: <kebab-case>            # identificador único, usado em [[id]]
title: <título legível>
domain: grant | partners | brazil | intelligence | proposal | meta
status: verified | partial | to-confirm
confidence: high | medium | low
last_updated: 2026-06-11
related: [<id>, <id>]       # componentes conexos
sources: [<url>, ...]       # fontes primárias (quando aplicável)
---
```

### Status

| Status | Significado |
|--------|-------------|
| `verified` | Confirmado em fonte primária (edital, lei, página institucional) |
| `partial` | Parcialmente confirmado; há lacunas marcadas no corpo |
| `to-confirm` | Hipótese ou dado de terceiros — **validar antes de citar em documento oficial** |

### Cross-links

Use `[[id]]` para apontar para outro componente. Links liberais são bem-vindos — um `[[id]]` ainda inexistente marca algo a documentar depois.

---

## Estrutura de pastas

```
context/
  README.md                         # este arquivo (manifesto)
  INDEX.md                          # mapa-mestre de todos os componentes
  sources.md                        # registro central de fontes/URLs
  grant/                            # as regras do edital
    overview.md
    eligibility.md
    assessment-criteria.md
    budget-and-costs.md
    timeline.md
    tne-strategy.md
  partners/                         # quem está na mesa
    team.md
    perryman.md
    tessarolo.md
    battestin.md
    cefor-ifes.md
    ou-iet.md
  brazil/                           # o contexto-país
    regulatory-recognition.md
    capes-globaledu.md
  intelligence/                     # leitura estratégica
    winning-patterns.md
    blind-spots.md
  proposal/                         # a tese e o plano
    recommended-direction.md
    path-options.md
    open-questions-and-next-steps.md
```

---

## Aviso de fidelidade

Os **perfis das pessoas** foram montados por pesquisa de fontes públicas (páginas institucionais, ORCID, Google Scholar, Lattes/Escavador). Trate dados marcados `to-confirm` como provisórios e valide com os próprios antes de citar em documento oficial. Os **índices e notas de aprovação** dos caminhos são estimativa própria de apoio à decisão, não números oficiais do British Council.

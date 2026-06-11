# CONTEXT.md — roteamento do vault `cefor-ou-tne`

Mapa de carga de contexto: onde mora cada coisa, o que carregar quando, e qual a fase ativa. Desenho e racional completos em [`cefor-ou-tne-workspace-spec.md`](cefor-ou-tne-workspace-spec.md).

## Fase ativa

**`bid` — candidatura.** Cutoff interno **27 jun 2026**, submissão pela OU **6 jul 2026**. Camada quente: `40-operacional/41-bid/`. `42-delivery/` está **DORMENTE** até a aprovação (dez 2026).

Próximo artefato: **concept note** (`41-bid/01-concept-note/`), em EN com resumo PT, alimentado pelo que estiver em `/20` e `/30a`.

## Camadas e quando carregar

| Camada | Pergunta | Carrega quando |
|---|---|---|
| `00-inbox/` | O que não posso perder agora? | Captura no calor da hora; revisitar a cada sessão (fase 1) |
| `10-literatura/10.1-documentos/` | O que a fonte diz? | Ao precisar do texto fiel do edital, Guidance v2, Grant Agreement, briefing, marco MEC |
| `10-literatura/10.2-conceitos/` | Qual o conceito atômico? | Ao manejar com precisão TNE, stackability, equivalência de crédito, RPL |
| `20-permanent-notes/` | O que pensamos sobre isso? | Ao escrever seção b e qualquer texto que dependa da leitura do time |
| `30-sintese/30a-map-of-content/` | Como o time entende o domínio? | `MOC-reconhecimento-tne.md` é o rascunho permanente da seção b |
| `30-sintese/30b-experiencias/` | O que a prática revelou? | Após cada reunião com IET/Leigh-Anne/Felipe |
| `40-operacional/` | O que executar e rastrear? | Sempre que o trabalho for produzir/rastrear candidatura ou WP |

## Regras de carga

- **Constraints sempre.** Todo texto que vai pra fora carrega `40-operacional/_config/constraints/` (compliance BC, LGPD/UK GDPR, EDI/acessibilidade, limites de palavra, escopo exploratory). Pensamento nas camadas de conhecimento **não** tem constraint de forma.
- **Ao retomar:** abrir primeiro `40-operacional/_memoria-cefor-ou-tne.md`. Crítico na fase 2 (pausas de semanas).
- **Source of truth de pendências:** `40-operacional/_pontos-a-definir-cefor-ou-tne.md` (IDs estáveis A1, A2...).
- **Plano vivo:** `40-operacional/_planejamento-cefor-ou-tne.md`.

## Fluxo que importa

reunião com IET (`/30b`) → insight (`/00`) → Permanent Note (`/20`) → MOC (`/30a`) → texto da seção b (`/40/41-bid/03`).

## Rituais

- **Inbox:** a cada sessão na fase 1; semanal na fase 2.
- **MOC:** revisar a cada marco ou reunião com o IET.
- **Memória + catálogo:** atualizar ao fim de cada sessão (LLM rascunha, autor confere).

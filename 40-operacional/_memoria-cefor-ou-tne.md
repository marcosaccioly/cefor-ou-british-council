# Memória — cefor-ou-tne

Cronológica reversa. Primeiro doc a abrir ao retomar. Cada entrada referencia a fase (`bid` ou `delivery`). LLM rascunha ao fim de cada sessão; autor confere.

---

## 2026-06-11 · fase `bid` · PIVÔ DE DIREÇÃO (canônico: Vanessa)

**Mudança de escopo importante.** Áudios da Vanessa (para Marquito e Elton) + email Vanessa→Felipe (cópia Marquito), processados da inbox. A direção do projeto **mudou** em relação ao material do Elton/`/30a`:

- **Reunião Vanessa + Felipe + Leigh-Anne** (véspera do feriado) reorientou a proposta. A Leigh-Anne puxa forte para **sustentabilidade / clima / EDI**; o edital reforça gênero e ambiental. A Vanessa reancorou tudo no **foco em EaD** (CEFOR e IET): grupos vulneráveis (aldeias indígenas, economia do mar/Piúma, educação ambiental/CIMAT) entram como **futuros usuários/públicos** mapeados, não como objeto direto.
- **A microcredencial SAIU** (A6). A nova versão (Felipe + IA) trocou o "blueprint de microcredencial" por **mapeamento institucional/temático dos campi do IFES**. → Isso **supera** a tese do Elton (`recommended-direction.md` "Caminho 1: microcredencial inclusiva com reconhecimento BR-UK") e os rascunhos de `41-bid` ancorados nela.
- **Objetivos 5 → 4** (A7); **atividades 7 → 5** (A8). Listas finais no email arquivado.
- **Felipe deu ok** às alterações da Vanessa. **Direção canônica = Vanessa** (decisão do time, registrada por Marquito). Falta a validação final da Leigh-Anne (A9).

**Alerta estratégico (A10):** sem a microcredencial, a seção B (núcleo de TNE e reconhecimento, ~35%) perde a âncora. Redefinir o núcleo de TNE que sustenta Quality & Relevance.

### Pendências que saem desta sessão

- ~~Destrinchar as 5 atividades~~ ✅ feito (`activities-and-mande.md` v2, campos do formulário real, drafts EN ≤50 palavras, `TBD` para o time).
- **Descoberta na re-análise:** `_versao-ou/…OU2.md` é **o formulário vivo** (Good Grants), não anexo: Purpose e objetivos novos já preenchidos; atividades ainda são as 5 do Felipe (a substituir pelas da Vanessa); campos reais por atividade = Type (dropdown fixo) + Description/Output/Indicator de ≤50 palavras.
- Divergência: objetivo 1 no OU2 está mais curto que no email da Vanessa (canônico = email). Atualizar no formulário.
- Drafts superados sinalizados com banner: `concept-note`, `gender-edi` (→A11, GATE), `sustainability-pathway`, `risks`.
- Resolver com o time: A10 (núcleo de TNE), **A11 (mecanismo de gênero pós-pivô — GATE)**, A12 (Activity Type/agrupamento da Atividade 3).

---

## 2026-06-11 · fase `bid` · integração do material do Elton

- Merge do repo do Elton (`vertumno/cefor-ou-british-council`, upstream) no fork. Ele mantinha uma versão paralela do projeto (mesma filosofia atômica, organizada por função: `context/` + `application/`).
- Material **reposicionado nas camadas** via `git mv` (histórico preservado): `application/` → `41-bid/` (que estava só com READMEs); `context/grant` → `10.1/grant-notes`, `context/brazil` → `10.2`, `context/partners` → `_config/partners`, `context/intelligence` → `/20`, `context/proposal` → `/30a`; versões OU2 → `41-bid/_versao-ou`; briefing v4 e análise → `10.1`.
- Notas que entraram em `/20` e `/30a` ganharam `author: elton` + marca `imported` (D4). **Nada do `_config` foi sobrescrito** — as versões ricas do Elton ficam lado a lado para consolidação.
- Fila de revisão humana registrada em [`00-inbox/_integracao-elton.md`](../00-inbox/_integracao-elton.md): consolidar `_config`, dar voz às notas importadas, migrar open-questions → catálogo, aposentar `_tracker` em favor dos docs vivos, escrever o MOC da seção b (tne-core).

### Pendências que saem desta sessão

- Processar a fila de `00-inbox/_integracao-elton.md` (6 itens).
- `git push origin main` quando autorizado (push direto foi bloqueado pela política).

---

## 2026-06-11 · fase `bid` · scaffold do vault

- Vault `cefor-ou-tne` materializado neste repositório git (`cefor-ou-british-council`). Estrutura de pastas, trio de docs vivos, `_config/`, slash command e `.gitignore` criados conforme a spec v2.
- Documentos oficiais da edição 2026 já estavam no repo e entraram em `10-literatura/10.1-documentos/`: Guidance **v2 2026**, Sample Application Form, Sample Grant Agreement, briefing interno (md + html v3) e link do edital.
- Ajustes registrados na seção 10 da `cefor-ou-tne-workspace-spec.md` (mapeamento raiz repo = raiz vault; A4 agora reconferível na Guidance v2 já presente).
- Mensagem de validação das 5 decisões com Vanessa e Elton pronta em `41-bid/_validacao-time.md`. **Aguardando respostas** (prazo sugerido: segunda 15/jun).
- Próximo artefato: concept note (`41-bid/01-concept-note/`), EN + resumo PT, caminho 1 (microcredencial de docência online inclusiva com reconhecimento BR-UK).

### Pendências que saem desta sessão

- Disparar a mensagem de validação para Vanessa e Elton (decisões D1–D5; itens A1, A2 do catálogo).
- Extrair via Docling os PDFs de `10.1` para notas de `10.2` e reconferir pesos 2026 (A4).

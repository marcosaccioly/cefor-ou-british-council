# Memória — cefor-ou-tne

Cronológica reversa. Primeiro doc a abrir ao retomar. Cada entrada referencia a fase (`bid` ou `delivery`). LLM rascunha ao fim de cada sessão; autor confere.

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

# Working Log

Diário de progresso do projeto. Entrada mais recente no topo.

---

## 2026-06-11 — Estruturação do workspace
- Pesquisa multi-fonte concluída (perfis, OU/IET, regulatório BR, padrões GGP, pontos cegos).
- Briefing **v4** publicado (`../../tne-briefing-v4.html`): critérios reais, perfis verificados, 4 caminhos com notas, índice clicável, pontos cegos.
- Base de conhecimento criada em `../../context/` (22 componentes).
- Workspace de redação criado em `application/` (form, concept note, atividades, gênero, orçamento, riscos, sustentabilidade, assets, trackers).
- Decisão central: **Caminho 1**.

### Próximos passos
1. Enviar as 3 perguntas ao British Council.
2. Fechar a microcredencial-âncora com a Leigh-Anne.
3. Refinar o `01-concept-note.md` e circular entre Vanessa/Felipe/Leigh-Anne.
4. CEFOR preenche dados reais (gênero, matrículas, CV da Vanessa).

---

## Backlog / ideias
- Confirmar OUVP para microcredenciais.
- Avaliar viabilidade do slot devolvido (Gales/Escócia/IN).
- Definir coorte do piloto (professoras — região/perfil).

---

## Nota técnica (manutenção da pasta)
O shell (git-bash) estava com erro de inicialização em 2026-06-11, então os PDFs e os briefings **não puderam ser movidos** para subpastas. Para relayout físico opcional, rodar no PowerShell (via prefixo `!` no terminal):

```powershell
# criar subpastas
New-Item -ItemType Directory -Force edital, briefing | Out-Null
# mover documentos oficiais
Move-Item "TNE Exploratory Grants 2026 *.pdf" edital\
# mover/arquivar briefings
Move-Item tne-briefing-v3.html briefing\
Move-Item tne-briefing-v4.html briefing\
```
Se mover, atualizar os caminhos no `README.md` da raiz.

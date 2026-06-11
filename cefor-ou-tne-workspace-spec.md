# Spec v2: Segundo Cérebro `cefor-ou-tne` -- CEFOR/IFES + Open University (IET)

**Demanda:** `cefor-ou-tne`
**Fontes:** `stages/01-listening/output/cefor-ou-tne-briefing.md` (briefing TNE Grant, 2026-06-11) + `_inbox/framework-conhecimento-pessoal.md` (framework segundo cérebro, abr-mai 2026) + `_inbox/templates-conhecimento-pessoal.md`
**Supersede:** a v1 desta spec (pipeline ICM pura espelhando o formulário). A pipeline não morreu: virou a camada operacional `/40` deste vault. v1 íntegra no histórico git.
**Nota de padrão:** híbrido consciente. As camadas de conhecimento seguem o framework Zettelkasten do Marquito (navegação por links, não por pastas), o que diverge do ICM clássico (folders as architecture). A camada `/40` continua ICM. Se o híbrido provar valor aqui, candidato a virar ficha em `knowledge-base/padroes/` via retro.

---

## 1. O que este workspace é

O vault do projeto TNE Exploratory Grant 2026 (CEFOR/IFES + IET/Open University), operado como segundo cérebro: o conhecimento que o time acumula sobre TNE, reconhecimento, regulatório e microcredenciais se acumula nas camadas de conhecimento; a candidatura e a execução do projeto rodam na camada operacional.

A aposta: a seção que mais pesa na avaliação (núcleo de TNE e ambiente regulatório, 35% de Qualidade) é exatamente onde conhecimento acumulado e interpretado rende mais que texto escrito às pressas. E a fase 2 (18 meses, poucas horas por semana, com pausas longas) é o caso de uso perfeito dos docs vivos: `_memoria` é o primeiro arquivo que se abre ao retomar.

## 2. Decisões de design

| # | Decisão | Racional |
|---|---|---|
| D1 | **Vault em português; artefatos que circulam com a OU em inglês** | As camadas de conhecimento são instrumento de pensamento do time CEFOR -- voz própria, em PT. Os outputs operacionais que vão pra Leigh-Anne (concept note, seções do formulário) nascem em EN dentro de `/40`. Felipe lê PT; pra Leigh-Anne, circula-se o EN |
| D2 | **Vault do lado CEFOR; OU consome exports** | O segundo cérebro não é o canal com a OU -- é onde o time pensa. O que cruza a fronteira é artefato exportado de `/40`. Se o Felipe quiser entrar no repo, ótimo, mas nada depende disso |
| D3 | **Camadas de conhecimento seguem o framework, sem fork** | `/00` a `/30` e `/50` idênticos ao framework pessoal (atomicidade, fidelidade de camada, voz progressiva, navegação por links). O que muda é o multi-autor: ver D4 |
| D4 | **Multi-autor com voz assinada** | Permanent Notes e MOCs ganham campo `author` no frontmatter (vanessa, elton, marquito). A voz da nota é de quem assina; discordância entre autores não se resolve editando a nota do outro -- escreve-se outra nota e linka-se a tensão. MOC pode ser co-autorado: é o estado do entendimento do TIME sobre o domínio |
| D5 | **Trio de docs vivos no lugar de decision log** | `_memoria`, `_pontos-a-definir` (catálogo com IDs estáveis A1, B5...) e `_planejamento`, conforme o framework. Decisões bilaterais fechadas viram item "Resolvido" no catálogo + entrada na memória. Sem pasta `decisions/` separada -- era redundante com o que vocês já praticam |
| D6 | **Constraints vivem na camada operacional** | Compliance British Council, LGPD/UK GDPR, EDI/acessibilidade, limites de palavra e o guarda "exploratory ≠ rodar curso" protegem os OUTPUTS -- então moram em `/40/_config/`, carregadas em todo texto que vai pra fora. As camadas de conhecimento não têm constraint de forma: pensamento é livre |
| D7 | **Ponte conhecimento -> candidatura é explícita** | Cada seção do formulário em `/40/41-bid/` referencia por wikilink as Permanent Notes e 1.2 que a embasam. Rastreabilidade: o avaliador pergunta "de onde vem essa afirmação sobre o marco regulatório?", a resposta está a um link de distância |
| D8 | **Sem segredos no repo** | Repo git privado. Credenciais fora; `.env` no `.gitignore` desde o commit zero. `.obsidian/` fora do versionamento |

## 3. Folder map

```
cefor-ou-tne/
├── CLAUDE.md                          # orientação: o que é, convenções de commit, papel da LLM
├── CONTEXT.md                         # roteamento: camadas, regras de carga, fase ativa
├── 00-inbox/                          # captura bruta, sem formato. Única regra: revisitar
├── 10-literatura/
│   ├── 10.1-documentos/               # extração fiel: edital, Guidance Notes, Grant Agreement,
│   │                                  #   marco MEC de microcredenciais, papers do IET, docs OU
│   └── 10.2-conceitos/                # nós atômicos: TNE, microcredencial empilhável,
│                                      #   equivalência de crédito, stackability, RPL...
├── 20-permanent-notes/                # voz própria assinada: "o que pensamos sobre
│                                      #   reconhecimento BR-UK", "onde o marco MEC aperta"...
├── 30-sintese/
│   ├── 30a-map-of-content/            # MOC-reconhecimento-tne.md: estado do entendimento
│   │                                  #   do time sobre o domínio. Evolui a cada nota nova
│   └── 30b-experiencias/              # reuniões com IET, sprints de co-desenho, piloto:
│                                      #   conceitos ativados + o que a prática revelou
├── 40-operacional/                    # camada Top-Down (ICM). Contexto, não conhecimento
│   ├── _memoria-cefor-ou-tne.md       # cronológica reversa; primeiro doc ao retomar
│   ├── _pontos-a-definir-cefor-ou-tne.md  # catálogo source-of-truth, IDs estáveis
│   ├── _planejamento-cefor-ou-tne.md  # plano vivo: fases, marcos, dependências
│   ├── _config/
│   │   ├── project-charter.md         # título, propósito, objetivos, ODS
│   │   ├── team.md                    # os 5, papéis, financiado vs in-kind
│   │   ├── governance.md              # comitê diretor, direitos de decisão OU/CEFOR
│   │   ├── deadlines.md               # 6 jul 26, 15 dez 26, 31 ago 27, 30 jun 28
│   │   └── constraints/               # scope-exploratory, compliance-bc, data-protection,
│   │                                  #   edi-accessibility, bilingual-writing
│   ├── 41-bid/                        # ATIVA: candidatura até 6 jul (cutoff interno 27 jun)
│   │   ├── 01-concept-note/           # alinha o time; circula com Leigh-Anne e Felipe (EN)
│   │   ├── 02-identity-objectives/    # seção a do formulário
│   │   ├── 03-tne-core/               # seção b -- AQUI a ponte com /20 e /30a paga o projeto
│   │   ├── 04-activities-monitoring/  # seção c
│   │   ├── 05-results-sustainability/ # seção d
│   │   ├── 06-gender-edi/             # seção e
│   │   ├── 07-budget-risks-ethics/    # seção f
│   │   └── 08-supporting-docs/        # seção g: carta IFES, carta OU, CVs
│   └── 42-delivery/                   # DORMENTE até aprovação (dez 2026)
│       ├── wp1-governance/            # wp2-recognition-mapping/, wp3-microcredential-codesign/,
│       └── ...                        # wp4-pilot/, wp5-reporting/, wp6-sustainability/
└── 50-assets/
    └── imagens/                       # prints da plataforma BC, telas, diagramas
                                       #   padrão YYYY-MM-DD_cefor-ou-tne-descricao.jpg
```

Omitido do framework: `/05-conhecimento-tecnico` (conhecimento técnico reutilizável entre projetos pertence ao vault pessoal de cada um, não ao vault do projeto) e a subdivisão `/40a-clientes` vs `/40b-negocio` (aqui o vault inteiro É um escopo operacional único).

## 4. Como as camadas servem ao projeto

| Camada | Pergunta | Uso concreto neste projeto |
|---|---|---|
| `/00` inbox | O que não posso perder agora? | Insight no meio de call com o IET, ideia de atividade, link que alguém mandou no grupo |
| `/10.1` | O que a fonte diz? | Guidance Notes 2026 conferidas contra as anteriores; marco MEC extraído via Docling; papers da Leigh-Anne sobre microcredenciais |
| `/10.2` | Qual o conceito atômico? | "Stackability", "equivalência de crédito", "TNE de microcredencial" -- os nós que a seção b do formulário vai precisar manejar com precisão |
| `/20` | O que EU penso sobre isso? | "Na minha leitura, o gargalo do reconhecimento não é o MEC, é a carga horária mínima da certificação IFES" -- assinada, datada, linkada |
| `/30a` MOC | Como o time entende o domínio? | `MOC-reconhecimento-tne.md` é o rascunho permanente da seção b. Quando chegar a hora de escrever o texto do formulário, ele já existe em estado bruto |
| `/30b` | O que a prática revelou? | Cada reunião com Leigh-Anne/Felipe vira experiência: conceitos ativados, o que o IET vê diferente, insights pro inbox |
| `/40` | O que executar e rastrear? | A candidatura e os WPs. Textos finais EN, constraints aplicadas, deadlines |

O fluxo que importa: **reunião com IET (`/30b`) -> insight (`/00`) -> Permanent Note (`/20`) -> MOC (`/30a`) -> texto da seção b (`/40/41-bid/03`)**. O mesmo ciclo na fase 2 alimenta o mapeamento de reconhecimento (wp2) e o relatório final.

## 5. Docs vivos e slash command

Conforme convenção do framework:

- **`_memoria-cefor-ou-tne.md`** -- cronológica reversa. Cada entrada referencia a fase (`bid` ou `delivery`). Primeiro doc a abrir ao retomar -- crítico na fase 2, que tem pausas de semanas.
- **`_pontos-a-definir-cefor-ou-tne.md`** -- catálogo com IDs estáveis. Já nasce com os itens da validação: A1 financiado vs in-kind, A2 carta IFES, A3 hospedagem do repo, A4 pesos 2026 a reconferir, A5 OU opera o repo ou recebe exports.
- **`_planejamento-cefor-ou-tne.md`** -- plano vivo. Nasce com o cronograma do briefing (cutoff 27 jun, submissão 6 jul, contrato 15 dez, relatórios ago/27 e jun/28).
- **`/status-cefor-ou-tne`** -- slash command em `.claude/commands/`, injeta memória + catálogo via `` !`cat` ``. Criado no scaffold, não requer manutenção.

## 6. Papel da LLM (adaptado do framework)

| Etapa | Autor | LLM |
|---|---|---|
| Decidir o que extrair das fontes (edital, papers, marco MEC) | ✓ | -- |
| Escrever Permanent Notes e MOCs | ✓ | -- (sugestão de conexões ok) |
| Rascunhar textos da candidatura em `/40` a partir do MOC e das notas | -- | ✓ (revisão obrigatória do autor da seção) |
| Verificar constraints (limites de palavra, EDI, escopo exploratory) | -- | ✓ |
| Traduzir/gerar resumos `-pt.md` e versões EN | -- | ✓ (revisão de quem assina) |
| Atualizar memória e catálogo após sessões de trabalho | -- | ✓ (conferência do autor) |

A linha do framework se mantém: o que instala conhecimento (interpretar, conectar, escrever em voz própria) é humano; o que é produção operacional (rascunho de formulário, tradução, tracking) a LLM acelera.

## 7. Rituais

- **Processamento do inbox:** semanal na fase 2; na fase 1 (até 6 jul), a cada sessão de trabalho -- o ciclo precisa girar em dias, não semanas.
- **Revisão do MOC:** a cada marco (submissão, contrato, cada WP fechado) ou reunião com o IET.
- **Memória + catálogo:** atualizar ao fim de cada sessão de trabalho (LLM rascunha, autor confere).

## 8. Questões abertas (= itens iniciais do catálogo)

| ID | Item | Encaminhamento |
|---|---|---|
| A1 | Financiado vs in-kind | Fechar com Vanessa e Elton antes do orçamento (mensagem de validação já enviada/pronta) |
| A2 | Carta do IFES | Vanessa aciona pró-reitoria esta semana |
| A3 | Hospedagem do repo | Sugestão: org do CEFOR/IFES, os 3 + Felipe como colaboradores |
| A4 | Guidance Notes 2026 | Reconferir pesos quando publicadas; ajustar ênfase do MOC se mudar |
| A5 | OU no repo ou via exports | Assumir exports (D2); convidar Felipe no primeiro contato |

## 9. Próximos passos

1. Scaffold do vault (Obsidian + git privado): pastas, trio de docs vivos pré-populados, `_config/`, slash command, `.gitignore`
2. Povoar `/10.1` com o que já existe: edital, Guidance Notes anteriores, Grant Agreement modelo, briefing interno
3. Concept note como primeiro output de `/40/41-bid/` -- alimentado pelo que já estiver em `/20` e `/30a`
4. Validação com Vanessa e Elton segue valendo (as 5 decisões não dependem da estrutura de pastas)
5. Retro no solution-design pós-submissão: avaliar se o híbrido segundo-cérebro + ICM operacional vira ficha em `knowledge-base/padroes/`

---

## 10. Nota de scaffold (2026-06-11)

Registro dos ajustes feitos ao materializar esta spec no repositório git, após comparar o desenho com os arquivos que já estavam no repo recém-criado.

- **Mapeamento de raiz.** O repositório no GitHub chama-se `cefor-ou-british-council`; o folder map da seção 3 usa `cefor-ou-tne/` como nó-raiz. Decisão: **a raiz do repo É a raiz do vault**. O slug `cefor-ou-tne` permanece nos nomes dos docs vivos (`_memoria-cefor-ou-tne.md`...) e no slash command (`/status-cefor-ou-tne`). O nome do repo não muda nada operacional.
- **`/10.1` já nasce povoado.** O passo 2 da seção 9 ("povoar /10.1 com o que já existe") foi parcialmente cumprido no próprio scaffold: o repo já trazia os documentos oficiais da edição 2026, então eles entraram direto em `10-literatura/10.1-documentos/`:
  - `TNE Exploratory Grants 2026 Call Guidance v2.pdf` (Guidance Notes **2026** — supera as "anteriores" citadas na spec; resolve parte do ponto A4: os pesos podem ser reconferidos nessa fonte, não mais "quando publicadas")
  - `TNE Exploratory Grants 2026 Sample Application Form.pdf`
  - `TNE Exploratory Grants 2026 Sample Grant Agreement.pdf`
  - `cefor-ou-tne-briefing.md` (briefing interno, fonte canônica em texto) + `tne-briefing-v3.html` (o mesmo briefing renderizado, v3) + `LINK-edital.txt`
  - Falta extração fiel (Docling) desses PDFs para notas de `10.1` e do marco MEC — segue como trabalho de povoamento, não de scaffold.
- **A4 atualizado.** Como a Guidance **v2 de 2026** já está no repo, a reconferência de pesos do A4 deixa de depender de publicação futura: é leitura dos PDFs presentes. Item mantido no catálogo, com encaminhamento ajustado.
- **`_validacao-time.md`.** A mensagem de validação das 5 decisões foi colocada em `40-operacional/41-bid/_validacao-time.md` (artefato operacional da fase bid). A seção "Registro pós-validação" dela alimenta `_memoria` e `_pontos-a-definir` quando as respostas chegarem.
- **Esta spec mora na raiz.** Como é a constituição do vault, `cefor-ou-tne-workspace-spec.md` fica na raiz, referenciada por `CLAUDE.md` e `CONTEXT.md`. Não foi para `/10.1` (que é para fontes externas, não para o nosso próprio desenho).
- **Tracking de pastas vazias.** Camadas ainda sem conteúdo recebem `README.md` curto descrevendo a função da camada (serve ao git e à fidelidade de camada do framework). Não há `.gitkeep` solto.

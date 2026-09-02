# AI_STATE — DO INÍCIO AO FIM

> **Última atualização:** 2026-09-02 (UTC)
> **Fonte de verdade para continuidade:** este arquivo + `content/catalog.yml` + pacote do conteúdo ativo.
> **Regra absoluta:** nenhum upload ou publicação no YouTube pode acontecer sem aprovação humana explícita e registrada.

## COMO ASSUMIR ESTE PROJETO

1. Leia este arquivo por inteiro, o `README.md`, `docs/DECISION_LOG.md` e `docs/PRODUCTION_PIPELINE.md`.
2. Rode `git status --short` para não sobrescrever trabalho existente. Nunca remova a raiz do repositório nem `.git`.
3. Confira `content/catalog.yml`; ele identifica o conteúdo ativo e o estado de cada entrega. Abra o `manifest.yaml` do item escolhido.
4. Para `GENESIS-001`, leia nesta ordem: `research/GENESIS-001/RESEARCH_BRIEF.md`, `content/long/GENESIS-001/outline.md`, `scripts/long/GENESIS-001/SCRIPT_DRAFT.md`, `content/long/GENESIS-001/metadata.md`.
5. Execute `python3 tools/validate_catalog.py`. Corrija inconsistências de dados antes de avançar estados.
6. Trabalhe somente na próxima etapa permitida pelo pipeline. Não pule revisão factual, avaliação de licença, QA ou aprovação humana.
7. Ao encerrar uma tarefa relevante, atualize: este arquivo, `CHANGELOG.md`, o manifesto/catálogo e os registros relacionados. Anote fatos, limitações e próximos passos — inclusive se nada foi produzido.

---

## STATUS ATUAL

- **Fase do programa:** Fundação documental e pré-produção do MVP.
- **Conteúdo ativo:** `GENESIS-001` — vídeo longo, pt-BR.
- **Estado do conteúdo ativo:** `SCRIPT` (rascunho criado; ainda não passou por revisão factual/narrativa independente).
- **Entregáveis existentes:** estrutura do repositório, documentação base, catálogo, pesquisa/outline/roteiro de Gênesis, metadados iniciais, backlog de Shorts e registries vazios.
- **Entregáveis inexistentes de propósito:** voz final, downloads de assets, música, SFX, timeline, legenda sincronizada, render, thumbnail final, upload e publicação.
- **Próximo portão:** revisão factual do roteiro de Gênesis contra o brief e as passagens listadas; registrar o resultado no manifest e no changelog.

## OBJETIVO DO PROJETO

Criar uma Content Factory editorial, progressivamente automatizável, que transforme conhecimento bíblico em narrativas audiovisuais de alta qualidade. O primeiro idioma é português brasileiro. O primeiro marco é um vídeo longo de Gênesis que possa ser avaliado para publicação; só após validação do processo haverá automação maior e expansão de idiomas.

## VISÃO

Fluxo-alvo: `pesquisa → roteiro → revisão → narração → assets → edição → legendas → thumbnail → metadados → revisão humana → publicação`.

A abordagem combina narrativa cinematográfica e documentário: começa pela história, explica contexto quando ele ajuda a compreensão e não se posiciona prioritariamente como pregação. A meta é uma biblioteca audiovisual coerente da criação ao Apocalipse — não volume automatizado.

## ARQUITETURA

A fonte de verdade está estruturada assim:

```text
Bíblia → livro → capítulo → evento → cena → roteiro → vídeo → derivados
```

- `content/catalog.yml`: índice editorial, identificadores, estado e relações de conteúdo.
- `research/<ID>/`: afirmações, referências, contexto e incertezas.
- `scripts/<formato>/<ID>/`: palavras autorais, cenas e notas de produção.
- `assets/registries/`: origem/licença/uso de mídia — um registro por item usado.
- mídia binária vive localmente e fica ignorada até haver decisão explícita de curadoria.
- idioma, voz, áudio, vídeo e metadados não são tratados como o mesmo dado; a arquitetura admite localização posterior.

## DECISÕES VIGENTES

| Decisão | Estado | Motivo / registro |
| --- | --- | --- |
| pt-BR é o idioma do MVP | aceita | validar uma audiência e workflow antes de localizar; `docs/MULTILANGUAGE.md` |
| Começar por `GENESIS-001` | aceita | primeiro marco editorial do projeto |
| Duração guiada por narrativa, não por meta rígida | aceita | alvo de produção 12–15 min para o MVP; pode variar após revisão |
| Roteiro autoral, sem reprodução extensa de tradução moderna | aceita | fidelidade com menor risco de copyright; `docs/EDITORIAL_GUIDELINES.md` |
| Publicação somente manual | inegociável | proprietário retém a decisão final; pipeline bloqueia automação |
| Nenhum asset sem registro de licença | inegociável | rastreabilidade e segurança jurídica |
| Automação somente depois do MVP avaliado | aceita | evitar automatizar processo não validado |
| Não escolher TTS/fornecedor agora | pendente deliberada | comparar licença, voz pt-BR e custo depois do roteiro aprovado |

## DECISÕES REJEITADAS / NÃO FAZER

- Não construir agora um pipeline de publicação automática ou conceder a uma integração poder de publicar.
- Não gerar dezenas de vídeos/Shorts antes de validar Gênesis.
- Não copiar capítulos bíblicos/traduções modernas em bloco para os roteiros.
- Não baixar mídia “encontrada na internet” sem licença/proveniência verificável.
- Não usar voz clonada ou imitação identificável de narrador real sem autorização.
- Não converter hipóteses, tradição ou harmonizações em fatos bíblicos.
- Não commit ar áudio, vídeo, projetos pesados, chaves ou arquivos `.env` por padrão.

## REGRAS EDITORIAIS E DE QUALIDADE

- A Bíblia é a fonte primária dos fatos narrados; cada cena mantém referências internas.
- Rotular camadas: **texto bíblico**, **contexto histórico**, **tradição/interpretação** e **incerteza**.
- Escrever em pt-BR natural, com cadência documental, gancho imediato e sem fórmulas genéricas de IA.
- Cada visual deve ser semanticamente alinhado à fala; não usar footage aleatório para preencher duração.
- Não tratar imagens geradas como prova histórica; registrar prompt, ferramenta e restrições.
- Aplicar todos os gates de `docs/QUALITY_CHECKLIST.md` antes de `HUMAN_REVIEW`.

## FERRAMENTAS E DEPENDÊNCIAS

| Item | Situação | Observação |
| --- | --- | --- |
| Python 3 padrão | em uso | somente para `tools/validate_catalog.py`; sem dependências externas |
| Git | em uso | memória e histórico operacional |
| TTS | não selecionado | avaliar licença comercial, pt-BR, voz masculina grave e portabilidade |
| Edição | não selecionada | escolher depois de aprovado roteiro e plano de assets |
| Stock / música / SFX | não selecionados | validar item a item, nunca por suposição de plataforma |
| YouTube API | não configurada | futura preparação permitida, publicação continua manual |

Nenhuma API, token ou credencial é necessária nesta fase.

## PIPELINE

Estados permitidos:

```text
IDEA → RESEARCH → OUTLINE → SCRIPT → SCRIPT_REVIEW → SCRIPT_APPROVED
→ VOICE → ASSETS → EDITING → QA → HUMAN_REVIEW → APPROVED → PUBLISHED → ANALYZING
```

- `SCRIPT_REVIEW` exige revisão factual e narrativa registradas.
- `SCRIPT_APPROVED` exige aprovação humana do roteiro antes de custo/geração de mídia.
- `HUMAN_REVIEW` exige pacote de QA completo.
- `APPROVED` exige decisão explícita do proprietário para aquele vídeo; não implica publicação automática.
- Detalhe e critérios: `docs/PRODUCTION_PIPELINE.md`.

## CONTEÚDOS PRODUZIDOS

Nenhum vídeo, áudio, thumbnail, asset ou publicação foi produzido nesta etapa.

Produzidos apenas documentos de pré-produção do MVP:

| ID | Formato | Idioma | Estado | Local |
| --- | --- | --- | --- | --- |
| GENESIS-001 | longo | pt-BR | SCRIPT | `content/long/GENESIS-001/` e `scripts/long/GENESIS-001/` |

## CONTEÚDOS EM PRODUÇÃO

### GENESIS-001 — *Gênesis: Como Tudo Começou*

- **Escopo:** narrativa dos principais movimentos de Gênesis 1–50, conectando a criação à chegada da família de Jacó ao Egito.
- **Roteiro:** primeiro rascunho autoral dividido em 22 cenas; estimativa de 12–14 minutos.
- **Referências:** catalogadas por cena no script; brief de pesquisa inclui limites e pontos sensíveis.
- **Bloqueios:** revisão factual independente; decisão humana sobre abordagem interpretativa/escopo; seleção de TTS só após aprovação do texto; nenhum asset foi ainda pesquisado/baixado.
- **Derivados previstos:** 12 oportunidades de Shorts, ainda em `IDEA`.

## BACKLOG PRIORIZADO

1. **P0 — Revisar factualmente `GENESIS-001`.** Conferir cada cena com as referências, principalmente Gn 1–2, 6–9, 11, 15, 19, 22, 32, 37–50; separar narração e contexto.
2. **P0 — Fazer revisão narrativa e obter aprovação humana do roteiro.** Ajustar duração, tom, foco e metadados somente após as revisões.
3. **P1 — Avaliar e escolher TTS substituível.** Registrar licença/comercial, custo, teste de pronúncia e voz selecionada.
4. **P1 — Criar plano de assets para cenas aprovadas.** Pesquisar item a item; preencher registries antes de editar.
5. **P1 — Produzir áudio, edição, legendas, opções de thumbnail e pacote de QA de Gênesis.**
6. **P1 — Avaliar o MVP com dados de esforço, custo e qualidade; documentar lições.**
7. **P2 — Selecionar e produzir poucos Shorts derivados de Gênesis após o longo estar validado.**
8. **P2 — Criar pré-produção de `EXODUS-001` somente após aprendizagem do MVP.**
9. **P3 — Automatizar tarefas repetitivas aprovadas, etapa por etapa.**

## PROBLEMAS CONHECIDOS E SOLUÇÕES

| Problema / risco | Estado | Mitigação atual |
| --- | --- | --- |
| Não há proprietário/revisor designado no repositório | aberto | não inferir aprovação; pedir aprovação explícita em cada gate humano |
| TTS, editor e fontes de assets ainda não foram escolhidos | esperado | arquitetura modular; não criar lock-in antes do teste |
| Risco de interpretações controversas em Gênesis | aberto | roteiro usa linguagem de atribuição e exige revisão factual/teológica editorial |
| Direitos autorais e licença de mídia | controlado, sem assets | registry obrigatório, política e bloqueio de QA |
| Duração real do roteiro só será conhecida após teste de voz | esperado | a estimativa é provisória; recalibrar após voz aprovada |
| Não existem métricas de canal | esperado | canal ainda não publicou; modelo de coleta está documentado |

## PADRÕES OPERACIONAIS

### Estrutura do repositório

Consulte `README.md` e `docs/CONTENT_DATA_MODEL.md`. Arquivos de mídia são deliberadamente ignorados; metadados e proveniência são versionados.

### Padrões editoriais

Consulte `docs/EDITORIAL_GUIDELINES.md` e `docs/SCRIPT_GUIDELINES.md`. Nunca retirar qualificadores de incerteza durante a edição.

### Padrões de TTS

Voz masculina pt-BR, documental, madura, clara e não imitativa. Seleção baseada em amostra do roteiro, licença e possibilidade de migração; `docs/TTS_GUIDELINES.md`.

### Padrões de assets e edição

Rastreabilidade em CSV, licenças verificadas, IA rotulada, relação semântica cena–asset, movimento e edição a serviço da narrativa. Consulte `docs/ASSET_POLICY.md` e `docs/VISUAL_GUIDELINES.md`.

### Monetização

Foco inicial em YouTube/publicidade após validação. Nenhuma integração ou produto adicional antes de audiência e processo consistentes; `docs/MONETIZATION.md`.

## STATUS DA AUTOMAÇÃO

| Fase | Estado |
| --- | --- |
| A — pesquisa assistida | manual assistida por documentos |
| B — geração de roteiro | manual assistida; rascunho de Gênesis criado |
| C — geração de cenas | manual estruturada; modelo validado no rascunho |
| D a I — assets, TTS, edição, legendas, thumbnail, SEO | não iniciadas operacionalmente |
| J — pipeline completo | proibido por enquanto; depende de MVP avaliado |
| publicação | sempre humana; não automatizar |

## CHANGELOG RESUMIDO

- **2026-09-02:** Inicializada a fundação documental, arquitetura de conteúdo, registries de assets, modelos, validador e pré-produção de `GENESIS-001`.

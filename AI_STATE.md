# AI_STATE — DO INÍCIO AO FIM

> **Última atualização:** 2026-09-05 (America/Sao_Paulo)
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

- **Fase do programa:** Montagem interna iniciada: direitos Arena foram revisados, áudio v03 foi regenerado, cobertura v03 foi criada e a animática do primeiro capítulo foi renderizada.
- **Conteúdo ativo:** `GENESIS-001` — vídeo longo, pt-BR.
- **Estado do conteúdo ativo:** `ASSETS` (primeira animática interna de cenas 01–04 renderizada; dez imagens Arena atuais candidatas e sete lacunas visuais para os capítulos seguintes. Doze candidatas históricas não têm binário local e cinco imagens foram rejeitadas. O material Arena não está aprovado para corte final/comercial/publicação).
- **Entregáveis existentes:** estrutura do repositório, documentação base, catálogo, pesquisa/outline/roteiro de Gênesis, revisão interna v01, termos oficiais Arena revisados, áudio v03 interno em 10 segmentos com hashes/durações, plano, shortlist Pexels, três revisões visuais de IA, animática interna do capítulo 01, ferramenta reprodutível de render e registries atualizados.
- **Entregáveis inexistentes de propósito:** licença comercial/publicável para outputs Arena, QA humano completo do áudio, marcadores de edição por cena, música, SFX, capítulos 02–04, legenda sincronizada, corte final, thumbnail final, upload e publicação.
- **Próximo portão:** gerar/revisar sete substitutos visuais para cenas 06–09, 13, 15 e 19, renderizar os capítulos 02–04 e executar QA humano interno. Direitos comerciais Arena permanecem bloqueados pela fonte primária registrada.

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
| `voice-00` foi aprovada para edição de rascunho por decisão do proprietário | aceita condicionalmente | licença/custo/portabilidade Arena seguem pendentes para corte final; missão Kokoro encerrada |
| Direção visual cinematográfica/documental da primeira bateria Arena aprovada para exploração | aceita condicionalmente | orienta novos conceitos e QA interno, mas termos/custo/atribuição e uso comercial/YouTube de imagens Arena seguem pendentes |
| Termos oficiais Arena revisados em 2026-09-05 | aceita | limitam o serviço/output a uso pessoal ou interno e vedam exploração comercial; a confirmação do proprietário não substitui licença separada/termos do provedor ausentes |

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
| TTS | rascunho Arena v03 interno regenerado | `voice-00` cobre cenas 01–22 em 10 MP3s; QA e pontos de corte pendentes; termos oficiais permitem somente uso interno no estado atual |
| Edição | animática interna por FFmpeg | `tools/video/render_genesis_internal_chapters.py`; executável FFmpeg não é versionado; CH01 foi renderizado e CH02–04 aguardam cobertura |
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

Uma animática interna de vídeo foi produzida para o capítulo 01 (cenas 01–04). Há mídia efêmera de rascunho: dez segmentos de voz Arena e dez PNGs Arena atuais, cuja evidência persistente é documental. Nenhum material é liberado para corte final, distribuição, YouTube, upload ou publicação.

Produzidos também documentos de pré-produção do MVP:

| ID | Formato | Idioma | Estado | Local |
| --- | --- | --- | --- | --- |
| GENESIS-001 | longo | pt-BR | ASSETS | `content/long/GENESIS-001/` e `scripts/long/GENESIS-001/` |

## CONTEÚDOS EM PRODUÇÃO

### GENESIS-001 — *Gênesis: Como Tudo Começou*

- **Escopo:** narrativa dos principais movimentos de Gênesis 1–50, conectando a criação à chegada da família de Jacó ao Egito.
- **Roteiro:** 22 cenas, 1.617 palavras aproximadas e 12:30 de plano; revisão interna v01 aplicada e roteiro aprovado pelo proprietário em 2026-09-02 UTC para pré-produção.
- **Áudio:** rascunho Arena v03 das cenas 01–22 foi regenerado em 10 segmentos, hasheado e medido em 11:39,360 para montagem interna. QA detalhado e marcadores por cena permanecem pendentes; os termos oficiais atuais impedem liberação comercial/publicável.
- **Referências:** catalogadas por cena; brief e revisão registram limites e pontos sensíveis.
- **Bloqueios:** nova revisão se entrar contexto externo; termos oficiais Arena limitam áudio/imagem a uso interno até licença separada/termos do provedor identificados; sete substitutos visuais faltam aos capítulos 02–04; limites reais de cena, QA humano e aprovação final/publicação continuam pendentes.
- **Derivados previstos:** 12 oportunidades de Shorts, ainda em `IDEA`.

## BACKLOG PRIORIZADO

1. **P0 — Completar os sete substitutos visuais faltantes.** Cobrir cenas 06–09, 13, 15 e 19, registrar hash/QA e não reutilizar bins históricos ausentes.
2. **P0 — Renderizar e auditar os capítulos internos 02–04.** Juntar em ordem CH01→CH04 somente depois da revisão individual.
3. **P0 — Criar marcadores de limites para as 22 cenas ou regenerar arquivos individuais em armazenamento persistente.** Não aceitar timing proporcional como corte final.
4. **P0 — Obter licença comercial/publicável separada, identificação do provedor/modelo e termos aplicáveis se houver intenção de YouTube.** A fonte oficial atual não libera esse uso.
5. **P1 — Produzir legendas, opções de thumbnail e pacote de QA de Gênesis depois de direitos e edição serem resolvidos.
6. **P1 — Avaliar o MVP com dados de esforço, custo e qualidade; documentar lições.**
7. **P2 — Selecionar e produzir poucos Shorts derivados de Gênesis após o longo estar validado.**
8. **P2 — Criar pré-produção de `EXODUS-001` somente após aprendizagem do MVP.**
9. **P3 — Automatizar tarefas repetitivas aprovadas, etapa por etapa.**

## PROBLEMAS CONHECIDOS E SOLUÇÕES

| Problema / risco | Estado | Mitigação atual |
| --- | --- | --- |
| Identidade nominal do proprietário/revisor não é armazenada | controlado | aprovação do roteiro foi capturada via decisão Arena; continuar exigindo decisão explícita em cada gate humano |
| TTS, editor e fontes de assets ainda não foram escolhidos | esperado | arquitetura modular; não criar lock-in antes do teste |
| Risco de interpretações controversas em Gênesis | aberto | revisão interna v01 preservou qualificadores; proprietário pode exigir especialista antes de aprovar roteiro |
| Termos Arena não permitem o uso comercial pretendido | bloqueado para publicação | fonte oficial revisada limita a uso pessoal/interno e exige requisitos do provedor; manter somente animáticas internas até licença separada |
| Direitos/licença e disponibilidade de mídia | aberto | Pexels tem candidatos sem download; 12 imagens Arena históricas perderam o binário local e 10 atuais são internas. Não aprovar nem renderizar arquivo ausente |
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
| B — geração de roteiro | manual assistida; roteiro de Gênesis aprovado para pré-produção |
| C — geração de cenas | manual estruturada; modelo validado no rascunho |
| D — assets | cinco candidatos Pexels sem download; 12 candidatas IA históricas sem binário local, 10 candidatas IA atuais e 5 rejeitadas; sete substitutos ainda faltam |
| E — TTS | rascunho Arena v03 interno completo; QA detalhado/limites de edição e direitos bloqueiam entrega final |
| F a I — edição, legendas, thumbnail, SEO | animática interna CH01 renderizada; CH02–04, legendas, thumbnail e QA final não iniciados |
| J — pipeline completo | proibido por enquanto; depende de MVP avaliado |
| publicação | sempre humana; não automatizar |

## CHANGELOG RESUMIDO

- **2026-09-02:** Inicializada a fundação documental, arquitetura de conteúdo, registries de assets, modelos, validador e pré-produção de `GENESIS-001`.
- **2026-09-02:** Concluída revisão interna factual e narrativa v01 de `GENESIS-001`; aplicadas duas correções de precisão e movido o pacote para `SCRIPT_REVIEW`.
- **2026-09-02:** Proprietário aprovou o roteiro v01 de `GENESIS-001` para pré-produção via decisão Arena; criado plano de teste de TTS e movido o pacote para `SCRIPT_APPROVED`.
- **2026-09-02:** Proprietário escolheu `voice-00` como candidata de audição; gerada amostra curta local, criado plano de assets e movido o pacote para `VOICE`. Uso comercial/YouTube ainda não foi verificado.
- **2026-09-02:** Proprietário aceitou a qualidade sonora da candidata para teste longo condicional. Avaliadas alternativas de TTS; Kokoro local é a opção open-weight prioritária para teste, sem homologação final.
- **2026-09-02:** Proprietário aprovou o teste local Kokoro. Runtime isolado foi provisionado, mas a obtenção do artefato oficial falhou por TLS/SSL; nenhum áudio Kokoro foi gerado e a falha foi registrada.
- **2026-09-02:** Reexecução solicitada pelo proprietário confirmou erro `SSL_ERROR_SYSCALL` ao resolver o endpoint oficial do modelo; nenhum artefato não verificado foi usado.
- **2026-09-02:** Proprietário abortou a missão Kokoro e escolheu `voice-00` Arena para o rascunho de narração de Gênesis. Termos comerciais/YouTube continuam pendentes e impedem publicação.
- **2026-09-02:** Gerado lote 01 de rascunho Arena para as cenas 01–10 de Gênesis; hashes e caminhos registrados.
- **2026-09-02:** Gerado rascunho Arena integral das cenas 01–22 em dez segmentos; duração MP3 total 11:37, hashes e relações de cena registrados.
- **2026-09-02:** Proprietário aprovou o rascunho Arena para sourcing de assets e edição interna; `GENESIS-001` avançou para `ASSETS`.
- **2026-09-02:** Criada shortlist inicial de cinco vídeos Pexels com origem, autor, licença e uso proposto registrados como candidatos; nenhum download ou uso foi aprovado.
- **2026-09-02:** Geradas sete imagens IA para teste visual; seis candidatas foram mantidas e a primeira versão do jardim foi rejeitada por conter ruínas. Prompts, hashes, dimensões, cenas e limitações foram registrados.
- **2026-09-03:** Proprietário aprovou a direção visual cinematográfica/documental dos candidatos da v01 para exploração interna; a decisão não autoriza uso final/publicação.
- **2026-09-03:** Segunda bateria IA revisada e registrada: seis novas candidatas foram mantidas, quatro imagens foram rejeitadas (incluindo duas tentativas de cisterna inadequadas) e a cena 16 permanece lacuna de cobertura.
- **2026-09-05:** Revisados os termos oficiais Arena; uso pessoal/interno é permitido, mas exploração comercial do output não. A confirmação ampla do proprietário foi registrada sem contrariar a fonte primária.
- **2026-09-05:** Gerados dez novos conceitos IA, resolvida visualmente a cisterna seca da cena 16 e registrados novos hashes. Os binários de 12 candidatas históricas não estavam disponíveis localmente.
- **2026-09-05:** Regenerado áudio interno v03 em 10 segmentos e renderizada a animática interna CH01 (cenas 01–04); capítulos seguintes aguardam sete substitutos visuais.

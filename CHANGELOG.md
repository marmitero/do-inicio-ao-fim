# Changelog

Mudanças significativas do projeto. Datas em UTC.

## 2026-09-02 — Fundação editorial e MVP de Gênesis

- Iniciado o repositório operacional do projeto **DO INÍCIO AO FIM**.
- Definidos propósito, princípios editoriais, política de fontes, rastreabilidade e veto obrigatório de publicação humana.
- Criada a estrutura modular para conteúdo, pesquisa, roteiros, assets, áudio, vídeo e thumbnails.
- Criado o catálogo central de conteúdo e um modelo de estados de produção.
- Criada a documentação inicial: estratégia, arquitetura bíblica, cronologia, roteiro, TTS, visual, ativos, música, SEO, thumbnail, QA, multilíngue, monetização, pipeline e roadmap.
- Criado o pacote de pré-produção `GENESIS-001`: pesquisa, outline, roteiro autoral com cenas, metadados e backlog de derivados.
- Criados registries CSV vazios com cabeçalhos para assets, assets de IA, música e SFX; nenhum asset de mídia foi baixado ou aprovado nesta etapa.
- Adicionada validação local sem dependências do catálogo e de manifests.
- Realizada revisão interna factual e narrativa v01 de `GENESIS-001`, com matriz de referências por cenas e duas correções de precisão.
- Movido `GENESIS-001` de `SCRIPT` para `SCRIPT_REVIEW`; aprovação explícita do proprietário permanece obrigatória antes da produção.
- Roteiro v01 de `GENESIS-001` aprovado pelo proprietário via decisão Arena para pré-produção; criado plano de teste de TTS e estado atualizado para `SCRIPT_APPROVED`.
- Registrada audição do candidato `voice-00`, gerada uma amostra curta local ignorada pelo Git e criado plano de assets sem downloads; licença/custo de TTS permanecem pendentes.
- Qualidade sonora de `voice-00` aceita pelo proprietário apenas para teste longo condicional; documentada triagem de TTS e Kokoro local definido como candidata open-weight prioritária para teste, sem homologação final.
- Proprietário aprovou teste local Kokoro; ambiente isolado foi provisionado, mas a obtenção do artefato oficial falhou por TLS/SSL. Nenhum áudio Kokoro foi produzido; criada ferramenta reprodutível e log do bloqueio.
- Reexecução solicitada confirmou `SSL_ERROR_SYSCALL` no endpoint oficial do modelo. O bloqueio foi documentado em v02, sem usar mirrors ou artefatos sem proveniência.
- Missão Kokoro abortada por decisão do proprietário; `voice-00` Arena selecionada para rascunho de narração por cena. Termos comerciais/YouTube continuam bloqueando uso final/publicação.
- Gerado lote inicial de narração Arena `voice-00` para as cenas 01–10 de Gênesis; criado manifest com hashes e log de geração. Áudios continuam como rascunhos internos.
- Gerado rascunho integral Arena `voice-00` para as 22 cenas em 10 segmentos; duração MP3 medida em 11:37 e hashes/limites de edição registrados.
- Proprietário aprovou o rascunho Arena para pesquisa de assets e edição interna; `GENESIS-001` avançou para `ASSETS`, sem aprovação de publicação.
- Registrada shortlist inicial de cinco vídeos Pexels como candidatos de baixo risco visual; nenhum arquivo foi baixado, aprovado ou usado.
- Geradas e revisadas sete imagens Arena para o estilo visual de Gênesis: seis candidatas, uma rejeitada; prompts, hashes, dimensões, cenas e limitações foram registrados.

## 2026-09-03 — Direção visual aprovada e segunda bateria de conceitos

- Proprietário aprovou a direção visual cinematográfica/documental da primeira bateria Arena exclusivamente para continuidade de exploração e QA internos de assets.
- Geradas, abertas e revisadas dez imagens adicionais Arena; seis se tornaram candidatas e quatro foram rejeitadas por não atenderem o briefing ou por riscos visuais.
- Registrados prompts/especificações, hashes SHA-256, dimensões, tamanhos, cenas, status e limites dos assets `AI-ASSET-0008` a `AI-ASSET-0017`. As especificações de prompt de `0008`–`0014` são explicitamente marcadas como reconstruídas, pois as chamadas originais não haviam sido persistidas.
- A cena 16 continua sem cisterna seca candidata: `AI-ASSET-0013` foi rejeitado por prop não solicitado e `AI-ASSET-0016` por conter água.
- Nenhum conceito Arena foi liberado para uso comercial/YouTube, corte final, upload ou publicação; termos, custo e atribuição continuam gates separados.

## 2026-09-03 — Regra global de custo zero e terceira tentativa de cisterna (cena 16)

- Registrada a regra global **custo zero** (ADR-016): todo o processo de desenvolvimento e produção deve ser gratuito; o que for pago será substituído por alternativa gratuita semelhante ou gerado internamente. Regra documentada em `AI_STATE.md`, `DECISION_LOG.md` e nos princípios do `README.md`.
- Geradas duas novas tentativas de cisterna **seca** para a cena 16 (`AI-ASSET-0018`, vista de cima; `AI-ASSET-0019`, ângulo três-quartos), com brief explícito de poço vazio, sem água/reflexo e sem objetos não solicitados.
- Registrados prompt, dimensões (1376×768), tamanho e SHA-256 dos dois arquivos em `assets/registries/ai_asset_registry.csv` (inicialmente `pending_visual_review`, pois a revisão visual não pôde ser concluída pelo assistente naquele turno).
- Criada `ASSET_VISUAL_REVIEW_v03.md`; o proprietário revisou visualmente as duas imagens e **aprovou ambas como candidatas** (ADR-017), encerrando a lacuna de cobertura da cena 16.

## 2026-09-03 — Matriz de cobertura e candidatas para as cenas 02, 11, 12 e 21

- Criada a matriz de cobertura visual `ASSET_COVERAGE_v01.md`: 18 das 22 cenas já tinham candidato de asset (IA e/ou Pexels); as lacunas remanescentes eram as cenas 02, 11, 12 e 21.
- Geradas quatro novas candidatas IA para essas lacunas (`AI-ASSET-0020` a `AI-ASSET-0023`), com prompts, dimensões (1376×768), tamanhos e SHA-256 registrados em `assets/registries/ai_asset_registry.csv`.
- O proprietário revisou visualmente e **aprovou as quatro como candidatas** (ADR-018): as **22 cenas passam a ter ao menos um candidato de asset**. Nenhuma aprovação de corte final, termos ou publicação decorre disso.
- Revalidada a licença Pexels em 2026-09-03: segue **gratuita** e compatível com a regra de custo zero (uso comercial, atribuição não exigida, modificação permitida; proibições de uso ofensivo de pessoas identificáveis, venda de cópias inalteradas, endosso implícito, redistribuição em plataformas de stock e uso como marca).
- O download de stock permanece bloqueado por `SSL_ERROR_SYSCALL` no host oficial (`www.pexels.com`/`videos.pexels.com`) neste ambiente; a falha foi reproduzida e **não** será contornada com mirrors desconhecidos. Os cinco candidatos Pexels continuam `candidate`, sem download.

## 2026-09-03 — Versionamento de mídia no Git e revisão dos termos da Arena

- Registrada a política de versionar mídia e artefatos de trabalho no Git (ADR-019): binários gitignorados (PNGs e MP3s de rascunho) não persistiram entre sessões e foram perdidos. O `.gitignore` passa a ignorar apenas segredos e ruído de SO/ferramenta.
- Revisados os termos de uso da Arena (arena.ai, atualizados 2026-02-23) em `docs/ARENA_TERMS_ASSESSMENT_v01.md` (ADR-020): uso limitado a *"personal or internal business use"*; exploração comercial do Output é proibida; serviço gratuito atualmente. Voz/imagens Arena permanecem rascunho interno; publicação exige consentimento escrito ou substituição por ferramenta gratuita com licença comercial.
- Iniciada a regeneração da mídia perdida (6 imagens `AI-ASSET-0018`–`0023`) e da narração por cena, agora versionadas no Git.
- Regeneradas as 6 imagens perdidas com os mesmos prompts; hashes atualizados no `ai_asset_registry.csv` (novos renders — re-confirmação visual recomendada, pois os pixels diferem da instância aprovada).
- Regenerada a narração `voice-00` por cena em arquivos individuais persistentes: cenas 01–10 sintetizadas, com durações reais medidas por parser de frames MP3 (total 2:40,7) e hashes em `AUDIO_DRAFT_MANIFEST_v03.csv`. Cenas 11–22 ficam para a próxima rodada (limite de síntese por turno).

## 2026-09-04 — Duração recalibrada para ~6 min e narração por cena (11–20)

- Registrada a decisão ADR-021: priorizar um vídeo **coeso e fluido** em vez de longo e morto; alvo de ~6 min; se precisar alongar, ampliar a história (sem pausas demais nem frases lentas). A duração medida da narração (22 cenas ≈ 5:50) é compatível com o alvo.
- Sintetizada a narração `voice-00` das cenas **11–20** (arquivos individuais persistentes); durações reais medidas e hashes anexados a `AUDIO_DRAFT_MANIFEST_v03.csv`. Total cenas 01–20: **5:27,6**.
- Restam as cenas **21–22** para completar as 22 cenas por arquivo individual (limite de síntese por turno).
- Sintetizada a narração `voice-00` das cenas **21–22**; a narração por cena está **completa para as 22 cenas** (arquivos individuais persistentes). Duração total medida: **5:58,6**, com hash/bytes/sample rate/duração por cena em `AUDIO_DRAFT_MANIFEST_v03.csv`.
- P0 #3 (marcadores reais por cena) concluído: as 22 cenas têm arquivo individual com duração medida. Falta a escuta humana (QA) por cena.

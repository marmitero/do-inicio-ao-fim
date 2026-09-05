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


## 2026-09-05 — Animática interna por capítulos e revisão de direitos Arena

- Revisados os Termos de Uso oficiais Arena, versão indicada como 2026-02-23; a documentação registra uso pessoal/interno e restrição de exploração comercial do output, além de requisitos do provedor de IA.
- A confirmação do proprietário de que considerava os termos validados foi registrada, mas não foi usada para contradizer a fonte primária nem para liberar YouTube, distribuição, upload ou publicação.
- Criadas e revisadas dez imagens Arena adicionais (`AI-ASSET-0018`–`0027`), incluindo uma cisterna seca aprovada visualmente para a cena 16; hashes, dimensões, bytes, prompts e limites foram registrados.
- Detectada indisponibilidade local dos binários ignorados de candidatos `0001`–`0017`; seus registros permanecem preservados, mas foram marcados como indisponíveis para render até restauração ou substituição rastreada.
- Regenerado conjunto v03 de narração interna em dez segmentos, cobrindo cenas 01–22; manifest e hashes próprios registram que não é reprodução bit idêntica do lote v02.
- Adicionada ferramenta reprodutível de renderização interna com FFmpeg e renderizada a animática CH01 (cenas 01–04), em MP4 H.264/AAC 1280×720. Capítulos 02–04 aguardam sete substitutos visuais.

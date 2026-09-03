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

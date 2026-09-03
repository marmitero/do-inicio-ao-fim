# Log de geração de áudio v01 — GENESIS-001

> **Data:** 2026-09-02 (America/Sao_Paulo)
> **Fornecedor/voz:** Arena speech synthesis / `voice-00`
> **Uso:** rascunho interno de narração. Não é áudio aprovado para entrega ou publicação.

## Lote 01

Foram gerados com sucesso os blocos `SCN-GENESIS-001-01` até `SCN-GENESIS-001-10` a partir da narração autoral do roteiro. O lote contém **10 arquivos MP3**, com **1,275,618 bytes** no total. Os caminhos, hashes SHA-256 e estados por cena estão em `AUDIO_DRAFT_MANIFEST_v01.csv`.

As cenas `11–22` permanecem `pending_generation`: o serviço de síntese permite no máximo dez clips nesta sessão. Elas devem ser geradas em lote novo, mantendo a mesma voz e o mesmo padrão de nomes, sem alterar texto aprovado silenciosamente.

## Controles de qualidade ainda pendentes

- [ ] Escuta humana de cada bloco para dicção, ritmo, ênfase, pausas e palavras truncadas.
- [ ] Conferência de continuidade sonora entre os blocos e medição de duração real de cada arquivo.
- [ ] Correções de roteiro/pronúncia registradas antes de regenerar qualquer cena.
- [ ] Geração das cenas 11–22 e atualização deste manifest.
- [ ] Confirmação de termos comerciais/YouTube, custo e atribuição do ambiente Arena antes do uso em corte final.

## Limite de licença

O proprietário autorizou a geração do rascunho, mas os termos comerciais/YouTube da voz Arena não foram documentados. Portanto, os arquivos são adequados somente para validação interna de voz, ritmo e montagem. O gate de publicação continua bloqueado, conforme `TTS_PROVIDER_DECISION_v01.md`.

## Superseded status

The per-scene batch was a transient workspace output and is no longer available for continuation. Its hashes remain in the v01 manifest as historical generation evidence. `AUDIO_DRAFT_MANIFEST_v02.csv` and `AUDIO_GENERATION_LOG_v02.md` supersede it as the current complete, segmented audition draft.

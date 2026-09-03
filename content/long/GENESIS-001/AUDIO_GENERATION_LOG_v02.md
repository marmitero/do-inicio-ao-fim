# Log de geração de áudio v02 — GENESIS-001

> **Data:** 2026-09-02 (America/Sao_Paulo)
> **Fornecedor/voz:** Arena speech synthesis / `voice-00`
> **Uso:** rascunho interno integral de narração. Não é áudio aprovado para entrega ou publicação.

## Resultado

Foi gerado um rascunho integral de Gênesis em **10 segmentos MP3**, cobrindo todas as cenas `01–22`. A segmentação respeita o limite de dez clips por sessão de síntese:

| Segmentos | Cenas | Duração MP3 medida |
| --- | --- | --- |
| 01–06 | 01–12, em pares | 58,416s; 64,704s; 55,584s; 67,104s; 68,544s; 66,816s |
| 07 | 13–15 | 100,488s |
| 08 | 16–17 | 63,096s |
| 09 | 18–20 | 91,056s |
| 10 | 21–22 | 61,128s |

**Duração total dos arquivos:** 11:37 (696.936s).
**Tamanho total:** 2,790,114 bytes.
**Ritmo nominal:** aproximadamente 139 palavras/minuto, calculado sobre as 1.617 palavras estimadas do roteiro. Está dentro da faixa de planejamento, porém a aprovação depende de escuta humana.

`AUDIO_DRAFT_MANIFEST_v02.csv` contém texto-fonte, cenas cobertas, caminhos, SHA-256, tamanhos, frames MP3, taxa de amostragem e duração por segmento.

## Mudança em relação ao lote v01

O lote v01, por cena, foi uma saída de trabalho efêmera e não ficou disponível para continuidade entre sessões. Para que todo o roteiro pudesse ser audicionado no mesmo ciclo de síntese, v02 agrupa cenas contíguas. O manifest v01 permanece como histórico e deve ser tratado como `ephemeral_not_available`; v02 é a referência auditiva atual.

A segmentação **não** resolve os limites de edição: antes de uma timeline final, é necessário criar marcadores de entrada/saída de cada cena ou regenerar blocos individuais em armazenamento persistente. Não estimar timestamps de cena por suposição.

## QA pendente

- [ ] O proprietário ouve os 10 segmentos e aprova/reprova dicção, ritmo, pausas e naturalidade.
- [ ] Editor identifica os limites reais das 22 cenas para a timeline.
- [ ] Nomes e termos recebem correção fonética no roteiro caso necessário; qualquer regeneração é registrada.
- [ ] Termos comerciais/YouTube, custo e atribuição do ambiente Arena são confirmados antes de uso no corte final.
- [ ] Áudio final por cena/segmento fica em armazenamento adequado e rastreável antes de edição definitiva.

## Limite de licença

O proprietário autorizou o rascunho Arena. Os termos comerciais/YouTube ainda não estão documentados no projeto; por isso, estes MP3s são somente artefatos internos para validar a narração e o ritmo. Não usar em publicação até o gate de licença ser resolvido.

## Decisão do proprietário

Em 2026-09-02 (America/Sao_Paulo), o proprietário aprovou este rascunho segmentado para **pesquisa de assets e edição interna de rascunho**. A decisão não aprova QA de áudio, corte final, uso comercial/YouTube ou publicação.

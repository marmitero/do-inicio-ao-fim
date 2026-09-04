# Timeline de edição v01 — GENESIS-001 (draft)

> **Data:** 2026-09-04
> **Estado:** montagem draft v01 (produção interna, ADR-022). Render: `video/GENESIS-001/GENESIS-001_draft_v01.mp4`.
> **Tratamento:** Ken Burns suave (zoom in/out alternado), 1920×1080 @30fps, narração `voice-00` por cena, sem música/SFX ainda.

## Mapeamento cena → imagem → áudio

| Cena | Duração áudio (s) | Imagem primária | Observação |
| --- | --- | --- | --- |
| 01 | 14,28 | AI-ASSET-0006 | grão/armazém (Egito) |
| 02 | 13,97 | AI-ASSET-0020 | uma história, muitos começos |
| 03 | 20,35 | AI-ASSET-0001 | luz da criação |
| 04 | 14,33 | AI-ASSET-0007 | jardim |
| 05 | 14,83 | AI-ASSET-0008 | saída do jardim |
| 06 | 14,93 | AI-ASSET-0009 | campo dos irmãos |
| 07 | 16,18 | AI-ASSET-0003 | tempestade/arca |
| 08 | 17,90 | AI-ASSET-0010 | pós-tempestade/aliança |
| 09 | 16,44 | AI-ASSET-0004 | Babel |
| 10 | 17,50 | AI-ASSET-0005 | jornada de Abrão |
| 11 | 17,06 | AI-ASSET-0021 | tenda à noite/estrelas |
| 12 | 17,95 | AI-ASSET-0022 | bifurcação de estrada |
| 13 | 16,32 | **AI-ASSET-0005 (placeholder)** | aguardando AI-ASSET-0015 (monte e carneiro) |
| 14 | 17,23 | AI-ASSET-0005 | jornada/fuga |
| 15 | 17,45 | AI-ASSET-0012 | rio noturno |
| 16 | 15,72 | AI-ASSET-0018 | poço seco |
| 17 | 17,78 | AI-ASSET-0006 | cárcere/armazém |
| 18 | 15,74 | AI-ASSET-0006 | fome/irmãos |
| 19 | 17,38 | **AI-ASSET-0006 (placeholder)** | aguardando AI-ASSET-0017 (salão de reconciliação) |
| 20 | 14,28 | AI-ASSET-0005 | família no Egito |
| 21 | 17,90 | AI-ASSET-0023 | mãos/alimento |
| 22 | 13,10 | AI-ASSET-0006 | grão/horizonte (Êxodo) |

**Total narração:** 5:58,6 (358,63 s).

## Placeholders pendentes

- Cena 13: `AI-ASSET-0015` (mountain test, semiarid) — regeneração pendente (limite de geração de imagem por turno atingido em 2026-09-04).
- Cena 19: `AI-ASSET-0017` (reconciliation hall) — regeneração pendente.

Ao regenerar, atualizar `scripts/render_video.py` (dict `SCENE_IMAGE`), o hash no `ai_asset_registry.csv` e re-renderizar para v02.

## Notas de edição

- Sem música/SFX nesta versão (registries vazios; próxima etapa).
- Legenda draft em `video/GENESIS-001/GENESIS-001_draft_v01.srt`, com tempos proporcionais ao texto (requer revisão de sincronia palavra a palavra).
- Regra de custo zero (ADR-016): render com ffmpeg estático livre (via `imageio-ffmpeg`).

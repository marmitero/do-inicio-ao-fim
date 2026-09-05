# Montagem interna por capítulos v01 — GENESIS-001

> **Data:** 2026-09-05 (America/Sao_Paulo)
> **Estado:** animática interna em progresso; não é corte final nem autorizada para uso comercial, upload ou publicação.
> **Regra de uso:** voz e imagens Arena permanecem restritas a uso pessoal/interno conforme `docs/ARENA_TERMS_REVIEW_2026-09-05.md`.

## Estrutura de junção

Os quatro arquivos previstos preservam a ordem canônica das 22 cenas. Eles podem ser concatenados nessa ordem, sem sobreposição narrativa:

| Ordem | Arquivo de capítulo | Cenas | Blocos de áudio | Duração de áudio da regeneração v03 | Situação |
| --- | --- | --- | --- | --- | --- |
| 1 | `CH01_ORIGENS_E_O_JARDIM` | 01–04 | 01–02 | 120,504 s | **renderizado** como animática interna |
| 2 | `CH02_RUPTURA_RECOMECOS_E_BABEL` | 05–08 | 03–04 | 126,552 s | aguarda substitutos locais de 06–08 |
| 3 | `CH03_PROMESSA_E_A_CASA_DE_JACO` | 09–15 | 05–07 | 230,448 s | aguarda substitutos locais de 09, 13 e 15 |
| 4 | `CH04_JOSE_E_A_PROMESSA_ABERTA` | 16–22 | 08–10 | 221,856 s | aguarda substituto local da cena 19 |

Duração total estimada pela regeneração v03: **699,360 s (11:39,360)**. Ela não substitui marcação real de fronteiras das 22 cenas.

## Capítulo 1 produzido

- **Arquivo:** `video/GENESIS-001/internal-chapter-draft/GENESIS-001_CH01_ORIGENS_E_O_JARDIM_INTERNAL_DRAFT.mp4`
- **Conteúdo:** cenas 01–04, na ordem grãos/pergunta → jornada retrospectiva → criação → jardim.
- **Formato:** MP4 H.264/AAC, 1280×720, 24 fps, áudio mono 24 kHz.
- **Duração medida:** 120,500 s.
- **Tamanho:** 5.332.535 bytes.
- **SHA-256:** `6d20be8f770e1f54e558ca7711a4117b6b69e13406550af0426059db97ef7f8f`.
- **Verificação visual:** quadros de 00:00, 00:30, 01:00 e 01:30 confirmam o fade inicial e a progressão de jornada, criação e jardim. O primeiro quadro é preto por causa do fade de entrada de 0,25 s.

## Mapeamento visual planejado

| Capítulo | Cena → asset atual ou lacuna |
| --- | --- |
| CH01 | 01→0023; 02→0024; 03→0025; 04→0026 |
| CH02 | 05→0027; 06→**gerar campo/rebanho**; 07→**gerar arca/tempestade**; 08→**gerar céu pós-tempestade** |
| CH03 | 09→**gerar Babel**; 10→0024; 11→0019; 12→0020; 13→**gerar monte/lenha/carneiro**; 14→0021; 15→**gerar rio noturno** |
| CH04 | 16→0018; 17→0023; 18→0023; 19→**gerar interior de reconciliação sem rostos**; 20→0024; 21→0022; 22→0019 |

`0023`, `0024` e `0019` reaparecem apenas com função narrativa distinta, identificada acima; não há corte de stock aleatório.

## Método de render

`tools/video/render_genesis_internal_chapters.py` cria movimentos lentos de pan/zoom e fade por imagem, concatena os blocos de áudio e gera um MP4 por capítulo. O script exige FFmpeg externo e aceita `FFMPEG_BIN` para indicar o executável. O binário não é versionado.

A animática distribui a duração de cada bloco de áudio entre suas cenas proporcionalmente às durações previstas no roteiro. Isso mantém a sequência, mas é uma aproximação operacional, não marcador de edição amostra a amostra. Nenhum capítulo restante deve ser tratado como final antes de ouvir os blocos e marcar os limites reais.

## Próximos passos objetivos

1. Gerar, abrir, registrar e revisar os sete substitutos indicados como lacuna na tabela.
2. Renderizar CH02–CH04 somente com os candidatos existentes e seus hashes atuais.
3. Reproduzir cada capítulo internamente e registrar QA de imagem, áudio, ritmo, transições e coerência factual.
4. Resolver direitos/licenças por fonte antes de qualquer proposta de corte final ou distribuição.

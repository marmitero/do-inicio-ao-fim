# Modelo de dados de conteúdo

## Identificadores

- Vídeo longo: `<BOOK>-001`, por exemplo `GENESIS-001`.
- Vídeo superlongo: `BIBLE-001`.
- Short: `<PARENT>-S<NN>`, por exemplo `GENESIS-001-S01`.
- Cena: `SCN-<CONTENT_ID>-<NN>`, por exemplo `SCN-GENESIS-001-01`.
- Evento canônico: `EVT-<BOOK>-<NN>`, por exemplo `EVT-GEN-01`.
- Asset de terceiro: `ASSET-0001`.
- Asset gerado: `AI-ASSET-0001`.
- Música: `MUSIC-0001`; efeito: `SFX-0001`.

IDs não são reutilizados, mesmo se o item for descartado.

## Entidades e relações

```text
Book (GEN)
  └─ Event (EVT-GEN-01) ─ references[]
       └─ Scene (SCN-GENESIS-001-01) ─ asset_ids[]
            └─ Script segment / narration
Content (GENESIS-001) ─ scene_ids[] ─ derived_content_ids[]
Asset ─ used_by_content[] / scene_ids[]
Localization ─ content_id + language + voice + metadata + audio
```

## Manifesto mínimo de conteúdo

Cada pacote em `content/<formato>/<ID>/manifest.yaml` guarda: ID, tipo, idioma, título de trabalho, estado, dono/aprovadores, fontes, relações, entregáveis, gates e atualização. O catálogo central duplica apenas campos de navegação; o manifesto é a fonte detalhada.

## Estados

| Estado | Significado | Saída mínima |
| --- | --- | --- |
| IDEA | oportunidade não pesquisada | título de trabalho e hipótese |
| RESEARCH | fontes e fatos sendo reunidos | brief com referências e dúvidas |
| OUTLINE | arco e escopo definidos | outline aprovado internamente |
| SCRIPT | rascunho em escrita | cenas e referências internas |
| SCRIPT_REVIEW | revisão factual/narrativa | comentários e resolução documentados |
| SCRIPT_APPROVED | texto liberado pelo proprietário | aprovação explícita registrada |
| VOICE | TTS/gravação sendo testado/gerado | configuração e arquivo de áudio |
| ASSETS | plano e licenças em andamento | registry preenchido |
| EDITING | timeline em montagem | projeto/EDL e versão |
| QA | verificações finais | checklist preenchido |
| HUMAN_REVIEW | pacote submetido | link/arquivo + checklist |
| APPROVED | proprietário liberou publicação | registro datado da aprovação |
| PUBLISHED | publicação manual ocorreu | URL, data e metadados finais |
| ANALYZING | dados pós-publicação em análise | relatório de métricas/aprendizado |

A mudança de estado não substitui os gates. Consulte o pipeline.

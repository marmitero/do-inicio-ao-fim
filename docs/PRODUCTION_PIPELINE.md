# Pipeline de produção do MVP

## Visão de fluxo

```text
IDEIA → PESQUISA → OUTLINE → ROTEIRO → REVISÃO FACTUAL + NARRATIVA
→ APROVAÇÃO DO ROTEIRO → VOZ → PLANO/LICENÇA DE ASSETS → EDIÇÃO
→ LEGENDAS + METADADOS + THUMBNAILS → QA → REVISÃO HUMANA
→ APROVAÇÃO EXPLÍCITA → PUBLICAÇÃO MANUAL → MÉTRICAS → APRENDIZADO
```

A seta não permite pular os portões em nome de velocidade. Retornos são esperados: um erro de asset ou áudio pode devolver a entrega a roteiro, voz ou pesquisa.

## Portões e responsáveis

| Gate | Requisito | Registro | Pode aprovar |
| --- | --- | --- | --- |
| Pesquisa → outline | referências, escopo, contexto e dúvidas listados | research brief + manifest | editor/pesquisador designado |
| Outline → roteiro | arco claro e eventos selecionados | outline + manifest | editor |
| Roteiro → `SCRIPT_REVIEW` | cenas, narração e refs por cena | script draft | roteirista |
| `SCRIPT_REVIEW` → `SCRIPT_APPROVED` | revisão factual e narrativa resolvidas | checklist/comentários e manifest | proprietário (texto) |
| Voz/assets → edição | voz aceita; IDs e licenças dos assets planejados | testes, registries e plano de cenas | produtor/editor |
| Edição → `HUMAN_REVIEW` | render, legendas, metadados, créditos e QA completos | QA preenchido | responsável por QA |
| `HUMAN_REVIEW` → `APPROVED` | proprietário assistiu/revisou pacote final | aprovação explícita datada | proprietário |
| `APPROVED` → `PUBLISHED` | upload/configuração manual confirmados | URL e data | proprietário ou operador autorizado |

**Aprovação de roteiro não equivale à aprovação de publicação.** Ambas são independentes e registradas.

## Pacote mínimo de cada etapa

| Etapa | Artefato mínimo |
| --- | --- |
| Pesquisa | `research/<ID>/RESEARCH_BRIEF.md` |
| Outline | `content/<formato>/<ID>/outline.md` |
| Roteiro | `scripts/<formato>/<ID>/SCRIPT_DRAFT.md` |
| Voz | arquivo(s) por cena + configuração e duração real |
| Assets | registry + plano de uso/creditos |
| Edição | versão de trabalho, timeline/EDL exportável e notas |
| Legendas | SRT/VTT sincronizado e/ou versão incorporada |
| SEO | metadata com títulos, descrição, tags e capítulos reais |
| QA | checklist datado |
| Publicação | URL, data/hora, versão e confirmação humana |

## Registro de custo e tempo

Ao fim do MVP, registrar horas por etapa, custo direto, retrabalho, ferramentas, bloqueios e decisões. Sem esse relatório, não aprovar automação: a fábrica precisa melhorar um processo observado, não uma suposição.

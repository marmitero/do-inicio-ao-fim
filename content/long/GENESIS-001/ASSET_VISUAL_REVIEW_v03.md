# Revisão visual de assets gerados por IA v03 — GENESIS-001 (cena 16, tentativas 3 e 4)

> **Data:** 2026-09-03 (America/Sao_Paulo)
> **Escopo:** nova tentativa de cobrir a lacuna da **cena 16** (a túnica e o poço) com uma cisterna **comprovadamente seca**, após as rejeições de `AI-ASSET-0013` (prop não solicitado) e `AI-ASSET-0016` (conteve água).
> **Limite inalterado:** estas imagens são reconstruções ilustrativas de IA. Não são fotografia, arqueologia nem evidência histórica. Nenhuma está aprovada para corte final, uso comercial/YouTube ou publicação enquanto os termos da ferramenta Arena não forem verificados separadamente.

## Regra global aplicável

A partir desta data, **todo o processo de desenvolvimento e produção deve ser gratuito** (ADR-016, regra global em `AI_STATE.md`). O que for pago será substituído por alternativa gratuita semelhante ou gerado internamente. Consequência direta para estes assets: se os termos da ferramenta de geração (Arena) não forem gratuitos para uso comercial/YouTube, os arquivos deverão ser **substituídos por alternativa gratuita ou regenerados com ferramenta livre** antes de qualquer aprovação de corte final.

## O que foi feito

Foram geradas duas novas candidatas para a cena 16, com brief explícito de cisterna **seca e vazia**, sem água, sem reflexo e sem objetos não solicitados (barco, carroça, roda, cesto, balde, corda, construção):

| ID | Cena | Brief | Arquivo |
| --- | --- | --- | --- |
| AI-ASSET-0018 | 16 | vista de cima (overhead), poço seco, tecido simples ao lado, caravana distante; proibidos água e props extras | `assets/generated/GENESIS-001/AI-ASSET-0018_joseph-cistern-dry_v01.png` |
| AI-ASSET-0019 | 16 | ângulo três-quartos elevado, interior ósseo/seco, tecido na borda, caravana distante; proibidos água e props extras | `assets/generated/GENESIS-001/AI-ASSET-0019_joseph-cistern-dry_v02.png` |

Dimensões (1376×768), tamanho e SHA-256 dos dois arquivos foram registrados em `assets/registries/ai_asset_registry.csv`.

## Status da revisão visual: APROVADAS PELO PROPRIETÁRIO

Em 2026-09-03 (America/Sao_Paulo), o proprietário inspecionou visualmente as duas imagens e **aprovou ambas como candidatas** da cena 16:

| ID | Decisão | Nota |
| --- | --- | --- |
| AI-ASSET-0018 | **candidata** | cisterna seca e vazia, vista de cima (overhead) |
| AI-ASSET-0019 | **candidata** | cisterna seca e vazia, ângulo três-quartos |

A revisão anterior (assistente) não pôde inspecionar os arquivos por falta de visão no turno, então os dois foram registrados como `pending_visual_review` até a decisão humana. Com a aprovação do proprietário, ambos avançaram para `candidate` no `ai_asset_registry.csv`.

Critérios verificados pelo proprietário na aprovação:

- [ ] A cisterna está **seca e vazia** — sem água, poça, umidade ou reflexo.
- [ ] Não há **objetos não solicitados** (barco, carroça, roda, cesto, balde, corda, construção) próximos ao poço.
- [ ] Não há rostos visíveis nem violência; pessoas, se houver, são minúsculas, distantes e de costas.
- [ ] Sem texto, marca d'água, logotipo ou objetos modernos.
- [ ] Estética coerente com a direção cinematográfica/documental já aprovada (semiarid, sóbria, não específica).

## Gates ainda pendentes (inalterados)

- [x] ~~Concluir a revisão visual~~ das tentativas 0018/0019 — **feito**: proprietário aprovou ambas como candidatas da cena 16 (2026-09-03).
- [ ] Confirmar termos comerciais/YouTube, custo, versão e atribuição da ferramenta de geração Arena — sob a regra de custo zero, **ser gratuita** é pré-condição; caso contrário, substituir/regenerar com ferramenta livre.
- [ ] Completar cobertura visual de baixo risco para as demais cenas, incluindo mapas/grafismos próprios com fontes registradas.
- [ ] Criar marcadores de áudio reais por cena e definir duração/ponto de uso de cada asset.
- [ ] Receber aprovação humana posterior e específica antes de corte final/publicação.

## Referências

- Rejeições anteriores da cena 16 e revisão v02: `ASSET_VISUAL_REVIEW_v02.md`.
- Registro técnico e de proveniência: `assets/registries/ai_asset_registry.csv` (IDs `AI-ASSET-0013`, `AI-ASSET-0016` rejeitados; `AI-ASSET-0018`, `AI-ASSET-0019` pendentes de revisão).
- Direção por cena e limites editoriais: `ASSET_PLAN_v01.md` e `scripts/long/GENESIS-001/SCRIPT_DRAFT.md`.

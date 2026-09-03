# Revisão visual de assets gerados por IA v02 — GENESIS-001

> **Data:** 2026-09-03 (America/Sao_Paulo)
> **Escopo:** segunda bateria de conceitos depois de o proprietário aprovar a linguagem visual cinematográfica/documental da v01 para continuidade de exploração.
> **Limite inalterado:** estas imagens são reconstruções ilustrativas de IA. Não são fotografia, arqueologia nem evidência histórica. Nenhuma está aprovada para corte final, uso comercial/YouTube ou publicação enquanto os termos da ferramenta Arena não forem verificados separadamente.

## Decisão de direção visual registrada

O proprietário aprovou a **direção visual** dos seis candidatos da v01 como referência para seguir criando cobertura. Esta autorização é limitada à exploração e QA de assets para edição interna. Ela **não** aprova nenhum arquivo individual para corte final, nem confirma licença, custo, atribuição ou permissão comercial da Arena.

## Resultado por asset

| ID | Cena(s) | Resultado visual | Decisão |
| --- | --- | --- | --- |
| AI-ASSET-0008 | 05 | viajante anônimo junto a rio enevoado e luz distante; funciona como atmosfera posterior à saída, mas não mostra a saída/querubins literalmente | candidata de uso estreito |
| AI-ASSET-0009 | 06 | campo amplo com rebanho, agricultor e pastor distantes; sem violência gráfica ou faces identificáveis | candidata |
| AI-ASSET-0010 | 08 | paisagem úmida, luz após tempestade e arco nas nuvens; sem pessoas, texto ou objeto moderno visível | candidata para aliança/pós-tempestade |
| AI-ASSET-0011 | 13 | subida montanhosa, mas com cadeia alpina/nevada excessivamente específica | **rejeitada**; substituída por 0015 |
| AI-ASSET-0012 | 15 | margem de rio noturna, figura anônima de costas e acampamento distante | candidata apenas para noite/retorno; não para a luta de Jacó |
| AI-ASSET-0013 | 16 | cisterna, túnica e caravana distante, porém um objeto de madeira/bandas não solicitado distrai e parece barco/carro | **rejeitada** |
| AI-ASSET-0014 | 19 | interior abobadado de pedra com rostos em primeiro plano visíveis e arquitetura específica demais | **rejeitada**; substituída por 0017 |
| AI-ASSET-0015 | 13 | subida árida de calcário, lenha e carneiro distante; figuras de costas, sem violência | candidata |
| AI-ASSET-0016 | 16 | a revisão ainda trouxe água visível numa cisterna que deveria estar seca | **rejeitada**; requer nova geração corrigida |
| AI-ASSET-0017 | 19 | sala simples de adobe/madeira, mantimentos e grupos distantes de costas, sem rostos legíveis | candidata de estabelecimento; não encena revelação/abraço |

## Verificações realizadas

- Os dez PNGs da bateria v02 foram abertos e inspecionados visualmente.
- Dimensões, tamanho e SHA-256 dos dez arquivos foram incluídos no `ai_asset_registry.csv`.
- Não foi aceito nenhum arquivo com texto, watermark, marca moderna ou rosto identificável nos candidatos mantidos.
- Três problemas foram recusados em vez de racionalizados: geografia alpina/nevada (0011), objeto não solicitado (0013), rostos/arquitetura muito específica (0014). A revisão de cisterna (0016) também foi recusada porque contém água, contrariando o briefing.
- O prompt das chamadas originais 0008–0014 não foi preservado persistentemente antes deste registro. O registry contém uma **especificação reconstruída**, marcada como tal; 0015–0017 preservam o texto da solicitação feita. Essa limitação impede tratar os prompts reconstruídos como transcrição literal.

## Cobertura e lacunas

A bateria adiciona candidatos de baixo risco para cenas 05, 06, 08, 13, 15 e 19. A cena 16 ainda não possui um candidato de cisterna seca aprovado visualmente; deve receber uma nova geração e nova revisão. Isso não autoriza iniciar timeline: os marcadores reais das 22 cenas, termos Arena e cobertura completa/licenciada continuam gates obrigatórios.

## Gates ainda pendentes

- [ ] Confirmar termos comerciais/YouTube, custo, versão e atribuição da ferramenta de geração Arena.
- [ ] Gerar e revisar uma cisterna **seca** para a cena 16; manter 0013 e 0016 rejeitados.
- [ ] Completar cobertura visual de baixo risco para as demais cenas, incluindo mapas/grafismos próprios com fontes registradas.
- [ ] Criar marcadores de áudio reais por cena e definir duração/ponto de uso de cada asset.
- [ ] Receber aprovação humana posterior e específica antes de corte final/publicação.

## Referências

- Primeira bateria e revisão: `ASSET_VISUAL_REVIEW_v01.md`.
- Registro técnico e de proveniência: `assets/registries/ai_asset_registry.csv`.
- Direção por cena e limites editoriais: `ASSET_PLAN_v01.md` e `scripts/long/GENESIS-001/SCRIPT_DRAFT.md`.

# Matriz de cobertura visual v01 — GENESIS-001

> **Data:** 2026-09-03 (America/Sao_Paulo)
> **Objetivo:** dar visibilidade de quais das 22 cenas já têm candidato de asset e quais seguem em lacuna, para fechar o gate de cobertura antes da edição.
> **Regra:** candidato ≠ aprovado. Nenhum asset entra no corte final sem revisão visual, licença/termos (gratuitos, sob ADR-016) e registro com hash. `pending_visual_review` significa gerado/registrado, mas ainda sem decisão visual.

## Legenda de status

- `candidate` — revisão visual concluída e mantido como candidato de cobertura.
- `pending_visual_review` — arquivo gerado/registrado; revisão visual ainda não concluída.
- `rejected` — revisado e recusado.
- `—` — sem candidato nesta família.

## Matriz por cena

| Cena | Função visual | Candidatos IA | Candidatos stock (Pexels) | Status de cobertura |
| --- | --- | --- | --- | --- |
| 01 — O fim que abre a pergunta | grão/tecido, horizonte escuro → luz | AI-ASSET-0006 (candidate) | ASSET-0001, ASSET-0005 (candidate) | coberta |
| 02 — Muitos começos, uma história | linha orgânica ligando atos; atmosfera | AI-ASSET-0020 (candidate) | — | coberta (motion graphic original ainda previsto) |
| 03 — O mundo recebe forma | escuridão → luz, água, terra | AI-ASSET-0001 (candidate) | ASSET-0001 (candidate) | coberta |
| 04 — O jardim e o limite | jardim, folhagens, luz | AI-ASSET-0007 (candidate) | — | coberta |
| 05 — A escolha e a saída | sombras, saída do jardim | AI-ASSET-0008 (candidate) | — | coberta (uso estreito) |
| 06 — Dois irmãos, um campo vazio | campo, rebanho, silhuetas | AI-ASSET-0009 (candidate) | — | coberta |
| 07 — A arca antes da chuva | madeira, corda, céu carregado | AI-ASSET-0003 (candidate) | ASSET-0003, ASSET-0004 (candidate) | coberta |
| 08 — Águas, terra e aliança | chuva/água, arco-íris | AI-ASSET-0003, AI-ASSET-0010 (candidate) | ASSET-0003, ASSET-0004 (candidate) | coberta |
| 09 — Uma cidade, uma torre, muitos caminhos | tijolos, dispersão | AI-ASSET-0004 (candidate) | — | coberta |
| 10 — Uma promessa na estrada | estrada desértica, tenda | AI-ASSET-0005 (candidate) | ASSET-0002 (candidate) | coberta |
| 11 — Espera, aliança e uma casa improvável | tenda à noite, estrelas, mãos idosas | AI-ASSET-0021 (candidate) | — | coberta |
| 12 — Separação e nascimento | bifurcação de estrada, planície, tenda | AI-ASSET-0022 (candidate) | — | coberta |
| 13 — O monte e o carneiro | subida, lenha, carneiro | AI-ASSET-0015 (candidate) | — | coberta |
| 14 — A bênção disputada | estrada/tenda, luz onírica | AI-ASSET-0005 (candidate) | ASSET-0002 (candidate) | coberta (genérica de viagem) |
| 15 — Uma casa que vira povo | acampamento, rio noturno | AI-ASSET-0005, AI-ASSET-0012 (candidate) | — | coberta |
| 16 — A túnica e o poço | poço seco, tecido, caravana | AI-ASSET-0018, AI-ASSET-0019 (candidate) | — | coberta |
| 17 — Do cárcere ao palácio | cela, espigas, armazéns | AI-ASSET-0006 (candidate) | ASSET-0005 (candidate) | coberta |
| 18 — A fome traz os irmãos | sacos de grão, portas, pegadas | AI-ASSET-0006 (candidate) | ASSET-0005 (candidate) | coberta |
| 19 — O nome revelado | salão em sombras, abraço em silhueta | AI-ASSET-0017 (candidate) | — | coberta |
| 20 — Uma família no Egito | grupo viajando, rio/paisagem | AI-ASSET-0005 (candidate) | ASSET-0002 (candidate) | coberta |
| 21 — O último medo | mãos ao redor de alimento, horizonte noturno | AI-ASSET-0023 (candidate) | — | coberta |
| 22 — A história continua | grão em mãos, horizonte/rio, cartela Êxodo | AI-ASSET-0006 (candidate) | ASSET-0005 (candidate) | coberta |

## Resumo

- **Cobertas (candidate):** 22 de 22 cenas — todas têm ao menos um candidato de asset (IA e/ou Pexels).
- **Pendentes de revisão visual:** nenhuma (as candidatas 0020–0023 foram aprovadas pelo proprietário em 2026-09-03, ADR-018).
- **Rejeitadas e substituídas:** AI-ASSET-0002, 0011, 0013, 0014, 0016 (mantidas como rejeitadas).
- **Ainda previstas (não são "lacuna", são próximos passos):** mapa/grafismo original (02, 09, 10, 20), motion graphics de transição e cartela "Êxodo" (22), que serão produzidos internamente na fase de edição, com fonte cartográfica registrada e custo zero.

## Stock (Pexels) — estado

- Cinco candidatos permanecem `candidate` e sem download (`ASSET-0001` a `ASSET-0005`).
- Licença de plataforma **revalidada em 2026-09-03**: uso gratuito, atribuição não exigida, modificação permitida; proibições (uso ofensivo de pessoas identificáveis, venda de cópias inalteradas, sugestão de endosso, redistribuição em plataformas de stock, uso como marca) seguem válidas e são compatíveis com a regra de custo zero.
- Download continua bloqueado neste ambiente por `SSL_ERROR_SYSCALL` no host `www.pexels.com`/`videos.pexels.com` (reproduzido em 2026-09-03). **Sem contornar TLS com mirrors desconhecidos.** Os candidatos permanecem apenas como referência; o download/registro de arquivo + hash será retomado quando houver conectividade oficial.

## Gates pendentes (inalterados)

- [x] ~~Revisar visualmente `AI-ASSET-0020`, `0021`, `0022`, `0023`~~ — feito: proprietário aprovou as quatro como candidatas (2026-09-03, ADR-018).
- [ ] Confirmar termos comerciais/YouTube da ferramenta Arena e que sejam **gratuitos** (ADR-016); caso contrário, substituir/regenerar com ferramenta livre.
- [ ] Revalidar página/autor/item de cada candidato Pexels no momento de um download futuro e registrar arquivo + SHA-256.
- [ ] Criar marcadores de áudio reais por cena e definir duração/ponto de uso de cada asset.
- [ ] Aprovação humana específica antes de corte final/publicação.

# Avaliação dos termos de uso da Arena (v01) — uso comercial/YouTube de voz e imagem geradas

> **Data:** 2026-09-03 (America/Sao_Paulo)
> **Escopo:** registrar, de forma operacional, o que os termos da ferramenta Arena permitem para voz e imagens geradas neste projeto. **Isto não é parecer jurídico**; é uma revisão operacional que aponta red flags para decisão humana, conforme `docs/ASSET_POLICY.md`.
> **Fonte:** "Arena: Terms of Use Agreement" — Arena Intelligence, Inc., atualizado em **2026-02-23**. URL: <https://help.arena.ai/articles/5629909088-terms-of-use> (e <https://arena.ai/>). Consultado em 2026-09-03.

## Entidade correta

O projeto usa as ferramentas de geração de imagem e voz do ambiente **Arena Intelligence, Inc. (`arena.ai`)**. Outros "Arena" encontrados na web (Arena PAC em `arena.run`, Design Arena, Arena PLM/PTC, AlgoArena etc.) **não** são a entidade em questão e seus termos não se aplicam aqui.

## Cláusulas relevantes (resumo operacional)

| Tema | Cláusula | Texto essencial | Efeito para o projeto |
| --- | --- | --- | --- |
| Escopo de uso | §01 (Use of the Service) | *"your use of the Service must be limited solely to personal or internal business use"* | Uso público/comercial (publicar no YouTube) **não é** o uso autorizado por padrão. |
| Atividades comerciais | §03.5(G) (Content Restrictions) | Conteúdo não pode envolver *"commercial activities and/or sales … without Company's prior written consent"* | Monetização/publicação comercial exige **consentimento prévio por escrito** da Arena. |
| Exploração comercial do Output | §05(i) (User Conduct) | Proibido *"license, sell, rent, lease, transfer, assign, reproduce, mirror, distribute, host, otherwise commercially exploit … the Service, the Output"* | Explorar comercialmente o Output gerado é listado como **proibido**. |
| Propriedade do Output | §03 (Ownership of Content) | *"The Company does not claim ownership of any Content generated … by you, including your Inputs or Outputs"* | O usuário retém a titularidade do Output — mas isso **não** afasta a restrição de uso comercial. |
| Garantia do Output | §03 | Output é entregue *"as is"/"all faults"*; o usuário é o único responsável pelo uso | Reforça que risco de terceiros (direitos, semelhança, copyright) é do usuário. |
| Atribuição | §04.3 | Empresa pode identificar o usuário por **identificador anônimo**; não há obrigação explícita de crédito | Não há requisito de atribuição para o Output em si. |
| Custo | §08 (Fees) | *"Company currently offers the Service free of charge. However, we retain the right to charge"* | Hoje é **gratuito** (compatível com ADR-016), mas sem garantia de permanência. |

## Conclusão

1. **Custo:** atualmente gratuito → alinhado à regra global de custo zero (ADR-016), mas a gratuidade pode mudar a qualquer momento.
2. **Uso comercial/YouTube:** **não claramente permitido.** A ToS limita o uso a "personal or internal business use" e proíbe explorar comercialmente o Output; monetização no YouTube é uso comercial. → **Red flag: escalar para decisão humana** (regra de `docs/ASSET_POLICY.md`).
3. **Uso interno atual:** editar rascunho/planejar assets **sem publicar** é compatível com "internal business use"; portanto os rascunhos de voz e imagem Arena podem continuar como material de trabalho interno, mas **não** podem ir à publicação sem resolver o ponto 2.

## Caminhos possíveis (decisão do proprietário)

- **A — Consentimento escrito:** obter autorização por escrito da Arena para uso comercial/publicação no YouTube.
- **B — Substituição gratuita (alinhado a ADR-016):** trocar voz e imagens por ferramentas gratuitas cujas licenças permitam uso comercial, ex.: TTS open (Kokoro ou similar), geração/edição de imagem livre, e stock gratuito (Pexels/Pixabay, já compatível). A missão Kokoro anterior falhou por TLS no sandbox; pode ser retomada com artefato oficial quando houver conectividade.
- **C — Manter como rascunho:** continuar a pré-produção com os rascunhos Arena e decidir a substituição antes da edição final.

## Impacto nos registros

- Voz Arena (`voice-00`) e as imagens Arena (`AI-ASSET-*`) permanecem com status de **rascunho interno / candidata**, nunca `approved` para corte final, até que A ou B se resolva.
- `license_or_terms_url` do registry passa a referenciar este documento como evidência da revisão; `commercial_use_review` permanece `pending` (ou `restricted`, quando atualizado).

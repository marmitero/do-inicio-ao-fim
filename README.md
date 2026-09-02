# DO INÍCIO AO FIM

> Uma operação editorial e audiovisual para narrar a história bíblica — do início ao fim — com rigor, clareza e linguagem cinematográfica em português brasileiro.

## Estado atual

**Fase:** fundação + teste de voz e planejamento de assets do MVP
**Marco em curso:** `GENESIS-001` — *Gênesis: Como Tudo Começou*
**Publicação automática:** proibida. Todo vídeo precisa de aprovação explícita do proprietário.

Leia **[AI_STATE.md](AI_STATE.md)** antes de alterar ou continuar o projeto. Ele é a passagem de turno oficial entre pessoas e IAs.

## O que este repositório contém

| Área | Papel |
| --- | --- |
| [`docs/`](docs/) | regras editoriais, licenças, qualidade, arquitetura e decisões |
| [`content/`](content/) | catálogo e pacotes de conteúdo por formato/estado |
| [`research/`](research/) | dossiês factuais, referências e pendências de pesquisa |
| [`scripts/`](scripts/) | roteiros autorais, planos de cena e modelos |
| [`assets/registries/`](assets/registries/) | registros de proveniência e licença de cada asset |
| `audio/`, `video/`, `thumbnails/` | entregáveis locais; binários são ignorados por padrão |
| [`tools/`](tools/) | verificações locais pequenas e sem dependências pesadas |

## Princípios inegociáveis

1. **Qualidade > consistência > escala.** Não operar como content farm.
2. **A Bíblia é a fonte primária dos acontecimentos.** O roteiro é autoral e registra referências internas.
3. **Fato, interpretação, tradição e hipótese são rotulados.** Nunca se apresenta especulação como texto bíblico.
4. **Nenhum asset entra no corte final sem origem e licença registradas.**
5. **Nenhum vídeo é publicado sem revisão e aprovação humana explícita.**
6. **O conteúdo é independente do idioma.** Localizações, voz, áudio e metadados são camadas separadas.
7. **Decisões operacionais ficam no repositório, não apenas em conversas.**

## Começar ou retomar o trabalho

1. Leia [`AI_STATE.md`](AI_STATE.md), depois [`docs/DECISION_LOG.md`](docs/DECISION_LOG.md).
2. Localize o item no [`content/catalog.yml`](content/catalog.yml) e confirme seu estado.
3. Siga o portão da etapa atual em [`docs/PRODUCTION_PIPELINE.md`](docs/PRODUCTION_PIPELINE.md).
4. Use os modelos em [`docs/templates/`](docs/templates/) e [`scripts/templates/`](scripts/templates/).
5. Ao concluir uma etapa relevante, atualize `AI_STATE.md`, `CHANGELOG.md`, o catálogo e o pacote de conteúdo.
6. Execute `python3 tools/validate_catalog.py` antes de marcar uma entrega como pronta.

## MVP: Gênesis

O pacote editorial inicial está em:

- [brief de pesquisa](research/GENESIS-001/RESEARCH_BRIEF.md)
- [manifesto do conteúdo](content/long/GENESIS-001/manifest.yaml)
- [outline](content/long/GENESIS-001/outline.md)
- [roteiro e mapa de cenas](scripts/long/GENESIS-001/SCRIPT_DRAFT.md)
- [metadados e Shorts derivados](content/long/GENESIS-001/metadata.md)

O roteiro passou por revisão interna v01 e foi aprovado pelo proprietário para pré-produção. O pacote está em **`VOICE`**: uma candidata de voz foi testada, mas sua licença/custo ainda não foram verificados. Isso não autoriza publicação: voz final, assets, QA e uma aprovação final explícita continuam obrigatórios.

## Segurança e mídia

- Use `.env` para configurações e credenciais locais; `.env.example` só contém nomes de variáveis.
- Não versione renders, áudio final, downloads de banco ou projetos pesados sem decisão deliberada.
- Registre assets antes de usá-los; consulte [`docs/ASSET_POLICY.md`](docs/ASSET_POLICY.md).

## Escopo desta fase

Validar uma produção manual/semi-automática publicável de Gênesis, aprender com ela e só então automatizar. A arquitetura já prepara crescimento; ela não presume que automação complexa deva ser construída agora.

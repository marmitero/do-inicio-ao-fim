# Mapa de conteúdo — da Bíblia aos derivados

Este mapa transforma a arquitetura editorial em backlog navegável. Ele é um plano, não uma autorização para produzir tudo agora. Só `GENESIS-001` foi criado como pacote ativo.

```text
BIBLE-001 (superlongo: criação → Apocalipse)
 ├─ Pentateuco
 │   ├─ GENESIS-001 (ativo, SCRIPT)
 │   │   ├─ EVT-GEN-01 Criação → GENESIS-001-S01
 │   │   ├─ EVT-GEN-02 Jardim/queda → GENESIS-001-S02
 │   │   ├─ EVT-GEN-03 Caim/Abel → GENESIS-001-S03
 │   │   ├─ EVT-GEN-05 Dilúvio/Noé → GENESIS-001-S04/S05
 │   │   ├─ EVT-GEN-06 Babel → GENESIS-001-S06
 │   │   ├─ EVT-GEN-07 Chamado de Abraão → GENESIS-001-S07
 │   │   ├─ EVT-GEN-09 Abraão/Isaque → GENESIS-001-S08
 │   │   ├─ EVT-GEN-10 Jacó/Esaú e retorno → GENESIS-001-S09/S10
 │   │   └─ EVT-GEN-11/12 José e reconciliação → GENESIS-001-S11/S12
 │   ├─ EXODUS-001 (planejado após avaliação do MVP)
 │   ├─ LEVITICUS-001 (backlog)
 │   ├─ NUMBERS-001 (backlog)
 │   └─ DEUTERONOMY-001 (backlog)
 ├─ História de Israel → longos por livro/arco, derivados por evento
 ├─ Poesia e sabedoria → longos por livro/tema, derivados por pergunta/poema
 ├─ Profetas → longos contextualizados, derivados por mensagem/evento
 ├─ Evangelhos → longos por evangelho, derivados por episódio/ensino
 ├─ Atos e cartas → longos por livro/conjunto, derivados por evento/argumento
 └─ Apocalipse → longo com gênero/lentes explícitos, derivados por visão/tema
```

## Regra de desdobramento

Todo item novo precisa declarar: `parent_content_id` (quando derivado), evento(s), referências, pergunta editorial, idioma, estado, pacote de pesquisa, roteiro e gates. Não criar Short apenas porque um evento existe; selecione aqueles com arco próprio e valor autônomo.

## Ordem operacional

1. Validar `GENESIS-001` do roteiro à avaliação pós-publicação.
2. Escolher poucos Shorts derivados com base na qualidade do longo e viabilidade de assets.
3. Documentar tempo, custo, QA e aprendizado.
4. Abrir `EXODUS-001` com templates já testados.
5. Só após ciclos repetidos, planejar `BIBLE-001` superlongo e automações maiores.

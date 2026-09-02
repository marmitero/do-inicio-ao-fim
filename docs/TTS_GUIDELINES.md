# Diretrizes de narração e TTS

## Perfil desejado

Voz masculina em português brasileiro, grave sem excesso de artificialidade, madura, clara, documental, de dicção precisa e ritmo controlado. O objetivo é transmitir uma narrativa histórica, não imitar qualquer pessoa real.

## Critérios para escolher fornecedor

| Critério | Pergunta de aceitação |
| --- | --- |
| Licença | permite uso comercial monetizado no YouTube? A atribuição é clara? |
| Voz | soa brasileira, natural e adequada ao texto de teste? |
| Controle | permite ajustar ritmo, pausa, pronúncia e exportar formato útil? |
| Custo | é gratuito/open-source ou tem custo previsível por vídeo? |
| Portabilidade | o roteiro, timestamps e metadados sobrevivem à troca de fornecedor? |
| Ética | não clona nem imita voz identificável sem permissão? |

## Protocolo de teste

1. Escolha um trecho de 45–60 segundos do roteiro já aprovado, com nomes e mudanças emocionais.
2. Gere amostras com pelo menos duas alternativas compatíveis com a licença.
3. Avalie naturalidade, pronúncia, respiração/pausas, inteligibilidade, fadiga e duração real.
4. Registre ferramenta, versão, configuração, custo e resultado em `content/<ID>/manifest.yaml` e no log de produção.
5. O proprietário escolhe a voz antes de gerar todo o vídeo.

## Produção

- Gere em blocos identificados por cena e mantenha o texto fonte que originou cada arquivo.
- Preserve WAV/arquivo-fonte localmente quando possível e exporte versão de edição adequada.
- Não “conserte” no áudio uma frase factualmente problemática: retorne ao roteiro.
- Normalização, redução de ruído e compressão são etapas de QA; registre preset/ferramenta usada.

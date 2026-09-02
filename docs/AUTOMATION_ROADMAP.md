# Roadmap de automação progressiva

## Guardrail geral

Automatizar somente tarefas repetíveis que tenham qualidade validada manualmente. Toda automação deve ter saída revisável, logs, IDs estáveis e possibilidade de substituição. A publicação final permanece manual em todas as fases.

| Fase | Capacidade | Pré-requisito | Saída esperada | Estado |
| --- | --- | --- | --- | --- |
| A | pesquisa assistida | schema e fontes definidos | brief estruturado com lacunas | manual assistida |
| B | apoio ao roteiro | estilo/QA validados no MVP | outline e draft revisáveis | manual assistida |
| C | decomposição em cenas | roteiro aprovado | scenesheet validável | manual estruturada |
| D | descoberta/registro de assets | política e registry testados | candidatos, nunca uso automático | não iniciada |
| E | TTS por cena | voz/licença escolhidas | áudio + metadados + timestamps | não iniciada |
| F | montagem assistida | assets/áudio com IDs | timeline/EDL revisável | não iniciada |
| G | legendas | áudio final estabilizado | SRT/VTT e QA de texto | não iniciada |
| H | ideação de thumbnails | estilo e direitos validados | mockups para escolha humana | não iniciada |
| I | pacote SEO | padrões e dados de canal | metadata e alternativas | não iniciada |
| J | orquestração do pipeline | ciclos manuais mensurados | jobs com gates humanos | não iniciada |

## Critérios antes de cada fase

1. medir a versão manual em pelo menos um caso real;
2. documentar entradas, saídas, erro mais comum e critério de aceitação;
3. implementar o menor componente possível, sem travar fornecedor;
4. testar com conteúdo não publicado ou versão de trabalho;
5. comparar qualidade, tempo e custo com o processo manual;
6. manter revisão humana e rollback;
7. atualizar `AI_STATE.md`, o decision log e o pipeline.

## Não automatizar agora

- decisão teológica/editorial sobre ambiguidade;
- aprovação de fatos, licença ou qualidade;
- upload/publicação;
- seleção final de voz, thumbnail ou metadados;
- qualquer ação que consuma custo recorrente sem confirmação.

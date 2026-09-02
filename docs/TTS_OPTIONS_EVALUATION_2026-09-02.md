# Avaliação de opções de TTS — 2026-09-02

> **Objetivo:** triagem técnica e operacional para o MVP `GENESIS-001`.
> **Não é parecer jurídico.** Antes de uso final, confirmar termos da versão/arquivo baixado, dependências, eventuais atribuições e regras da plataforma na data de produção.

## Critérios eliminatórios

Uma opção não segue para a narração final se não for possível documentar:

1. licença compatível com uso comercial no YouTube para código, pesos e voz específica;
2. origem e versão exatas dos arquivos utilizados;
3. voz masculina pt-BR com qualidade aceitável em um trecho longo;
4. custo previsível e ausência de clonagem/imitação de pessoa identificável;
5. exportação local por cena e possibilidade de trocar de fornecedor.

## Opções pesquisadas

| Opção | Evidência verificada | Vantagem | Risco / lacuna | Decisão de triagem |
| --- | --- | --- | --- | --- |
| **Kokoro-82M v1, local** | O repositório oficial descreve pesos Apache e suporte a pt-BR; o card de vozes lista `pm_alex` e `pm_santa` como vozes masculinas pt-BR. | open-weight, local, duas vozes masculinas pt-BR documentadas, sem custo por caractere para inferência própria. | é preciso conferir licença do artefato baixado, dependências, qualidade real, hardware/tempo e atribuições antes do uso. | **candidata prioritária para teste técnico** |
| **Piper / vozes pt-BR** | A lista do projeto arquivado enumera vozes pt-BR, mas o projeto está read-only desde outubro de 2025. | histórico de execução local e opções pt-BR. | licença/proveniência deve ser analisada por voz/model card e runtime; projeto arquivado adiciona risco de manutenção. | não selecionar para MVP sem auditoria por artefato |
| **Arena `voice-00`** | O proprietário aprovou a sonoridade da amostra curta da sessão. | já atende inicialmente à preferência auditiva do proprietário. | identificador é de sessão; não há termos comerciais, custo, versão/modelo ou portabilidade documentados no repositório. | referência sonora; **não homologada para corte final** |
| **Coqui XTTS e similares** | Ferramenta e pesos podem ter licenças distintas; a discussão do próprio projeto alerta para verificar licença de cada modelo. | suporte multilíngue pode ser tecnicamente atraente. | não é o caminho de menor risco para o MVP sem licença de peso claramente comercial. | fora da shortlist inicial |

## Fontes consultadas

- Kokoro — repositório oficial e instruções de pipeline/pt-BR: <https://github.com/hexgrad/kokoro>
- Kokoro-82M — card de modelo, release v1, hash e condições apresentadas: <https://huggingface.co/hexgrad/Kokoro-82M>
- Kokoro-82M — lista oficial de vozes, incluindo `pm_alex` e `pm_santa`: <https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md>
- Piper — lista de vozes e estado de arquivamento: <https://github.com/rhasspy/piper/blob/master/VOICES.md>
- Coqui — lembrete de que licença de código e pesos pode variar: <https://github.com/coqui-ai/TTS/discussions/4042>

**Data de consulta:** 2026-09-02 UTC. URLs e termos precisam ser relidos no momento do download; registrar commit/hash, versão de pacote e evidências no log de produção.

## Recomendação operacional atual

1. Manter `voice-00` apenas como referência de timbre/cadência que o proprietário aprovou para teste.
2. Executar um teste local e descartável de **Kokoro-82M v1** com `pm_alex` e `pm_santa`, usando exatamente o texto de audição e mais um trecho de 45–60 segundos de Gênesis.
3. Antes de guardar áudio de produção, registrar versão, hash, licenças observadas, dependências, configuração e resultado por voz.
4. O proprietário escolhe a voz final somente depois de ouvir as amostras longas e de a licença estar marcada como verificada.
5. Se Kokoro não cumprir qualidade/pronúncia, avaliar a próxima opção com o mesmo protocolo — sem converter a amostra Arena em voz final por conveniência.

## Preparação técnica necessária para o teste local

O ambiente atual não possui `kokoro`, `torch`, `soundfile` ou executável `espeak-ng`. Não instalar dependências no repositório nem registrar pesos/modelos no Git. O teste deve usar ambiente isolado (por exemplo, virtualenv local/descartável), fixar versões e produzir somente áudio de teste ignorado pelo Git.

## Decisão pendente do proprietário

Escolher se o próximo teste deve priorizar o piloto local Kokoro com as duas vozes masculinas pt-BR ou se deve ser pesquisada outra solução com licença comercial explicitamente contratada. A aprovação sonora de `voice-00` não resolve essa decisão de fornecedor.

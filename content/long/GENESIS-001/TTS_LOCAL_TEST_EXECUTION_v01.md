# Execução de teste local de TTS v01 — GENESIS-001

> **Data:** 2026-09-02 UTC
> **Objetivo:** testar Kokoro-82M v1 em pt-BR com `pm_alex` e `pm_santa`, após decisão do proprietário de priorizar o caminho local open-weight.

## Ambiente tentado

| Campo | Registro |
| --- | --- |
| Ambiente | virtualenv descartável fora do repositório |
| Python | 3.11.2 |
| Pacote Kokoro instalado | 0.9.4 |
| Pacote soundfile instalado | 0.14.0 |
| Torch instalado | 2.14.0+cu130 |
| Modelo solicitado | `hexgrad/Kokoro-82M` |
| Idioma | `p` / pt-BR |
| Vozes solicitadas | `pm_alex`, `pm_santa` |
| Texto | `TTS_LONG_SAMPLE_v01.txt` (519 caracteres) |
| Saída esperada | WAV 24 kHz por voz, em diretório local ignorado pelo Git |

## Resultado

**BLOQUEADO POR AMBIENTE — nenhum áudio Kokoro foi gerado.**

O pacote foi instalado no ambiente isolado, mas o runtime não conseguiu obter `config.json` do repositório oficial do modelo. A tentativa falhou repetidamente com encerramento TLS/SSL durante a conexão com `https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/config.json`, seguido de `LocalEntryNotFoundError` porque não havia artefato no cache local.

A tentativa de obter `espeak-ng` pelo gerenciador de pacotes também não pôde concluir atualização de índices por falha de rede; o pacote não foi localizado. O pacote Python `espeakng-loader` foi instalado como dependência de `misaki`, mas a falha do download do modelo aconteceu antes de qualquer geração e não valida a cadeia fonética.

## Impacto e decisão

- Não houve download de pesos/vozes confirmados, hash de artefato, output de áudio, custo ou benchmark de qualidade Kokoro.
- Nenhum arquivo de produção foi criado, e `voice-00` continua apenas como referência sonora sem licença comercial documentada.
- A opção Kokoro **não está rejeitada**; está `blocked_by_network_artifact_download` neste ambiente.
- Não usar mirror aleatório, arquivo sem hash ou modelo de procedência não comprovada para contornar o bloqueio.

## Próxima tentativa segura

1. Usar máquina/rede que alcance a fonte oficial ou receber artefato offline verificado, com URL, versão e SHA-256 registrados.
2. Executar `tools/tts/kokoro_smoke_test.py` com as duas vozes pt-BR.
3. Registrar duração, hashes dos WAVs, velocidade, versões de dependência e escuta do proprietário em `TTS_AUDITION_LOG_v01.md`.
4. Revalidar licença/atribuição da versão de pesos/vozes obtida antes de aceitar qualquer resultado para o corte final.

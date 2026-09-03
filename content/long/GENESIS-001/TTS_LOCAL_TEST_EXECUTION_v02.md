# Execução de teste local de TTS v02 — GENESIS-001

> **Data:** 2026-09-02 (America/Sao_Paulo)
> **Solicitação:** reexecução do teste Kokoro aprovada pelo proprietário.
> **Resultado:** bloqueio de conectividade confirmado antes da obtenção do artefato; nenhum áudio Kokoro foi gerado.

## Preflight realizado

Foi consultado diretamente o endpoint oficial necessário ao runtime:

```text
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/config.json
```

Resultado da chamada de conectividade:

```text
curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to huggingface.co:443
```

Sem `config.json`, pesos e voicepacks oficiais no cache local, o `KPipeline` não pode ser iniciado legitimamente. Por isso, não foi feita uma nova instalação pesada de dependências e não foi usado mirror, pacote reempacotado ou arquivo de procedência não verificável.

## Estado dos outputs

| Item | Estado |
| --- | --- |
| `pm_alex` WAV de teste | não gerado |
| `pm_santa` WAV de teste | não gerado |
| hash do modelo/voicepack baixado | indisponível; artefato não obtido |
| hash de output | indisponível; nenhum output existe |
| avaliação auditiva Kokoro | pendente |
| áudio Arena de referência | era efêmero/ignorado pelo Git; não é entrega de produção |

## Conclusão

A reexecução confirmou que o bloqueio não é uma lacuna de roteiro ou da ferramenta `kokoro_smoke_test.py`, mas de acesso TLS do ambiente ao host oficial do artefato. O teste não deve ser marcado como aprovado, falho em qualidade ou concluído: ele permanece **não executável neste ambiente**.

## Retomada segura

Executar em uma máquina que acesse a origem oficial ou que possua artefatos obtidos oficialmente e acompanhados de versão, URL e SHA-256. Então:

```bash
python3 tools/tts/kokoro_smoke_test.py \
  --text-file content/long/GENESIS-001/TTS_LONG_SAMPLE_v01.txt \
  --output-dir audio/GENESIS-001/voice-test/kokoro \
  --voices pm_alex pm_santa \
  --speed 0.95
```

Após gerar os dois WAVs, preencher `TTS_AUDITION_LOG_v01.md` com hashes, duração, versões, achados de licença e a decisão auditiva do proprietário. Nenhum resultado deve seguir para narração integral sem esse registro.

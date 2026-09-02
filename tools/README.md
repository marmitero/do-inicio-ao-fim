# Ferramentas locais

## `validate_catalog.py`

```bash
python3 tools/validate_catalog.py
```

Executa verificações leves, sem dependências externas, do catálogo e dos campos críticos do manifesto. Ele não valida licenças, fatos bíblicos, qualidade de mídia, YAML arbitrário nem aprova publicação. Esses gates continuam humanos/documentais.

## TTS local

`tools/tts/kokoro_smoke_test.py` gera clips de audição em runtime isolado. Consulte `tools/tts/README.md`; não é uma ferramenta de produção nem instala dependências no repositório.

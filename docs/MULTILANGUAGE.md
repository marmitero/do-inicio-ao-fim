# Arquitetura multilíngue

## Estratégia

O MVP é exclusivamente `pt-BR`. Outros idiomas só entram depois de validar roteiro, voz, assets, edição, custo e desempenho. Tradução é localização editorial, não simples conversão literal de texto.

## Separação obrigatória

```text
Conteúdo canônico (eventos, referências, intenção)
  ├─ localização pt-BR: roteiro, voz, legendas, metadados
  ├─ localização en: roteiro adaptado, voz, legendas, metadados
  └─ localização es: roteiro adaptado, voz, legendas, metadados
```

O mesmo `content_id` pode ter localizações, mas cada versão recebe idioma, voz, revisão cultural, áudio, caption e metadados próprios. Não reaproveitar automaticamente título, thumbnail com texto, ritmo ou referência de tradução.

## Requisitos para abrir novo idioma

1. MVP pt-BR publicado e avaliado; processo e custos registrados.
2. Roteiro canônico/referências suficientemente estáveis.
3. Revisor fluente e critérios de adequação editorial definidos.
4. TTS ou narrador com licença e teste de pronúncia aprovados.
5. QA de legendas, metadados, créditos e direitos testado.
6. Decisão documentada em `docs/DECISION_LOG.md` e `AI_STATE.md`.

## Regras de localização

- Adaptar ritmo, idiomatismo, nomes transliterados e contexto para audiência, mantendo referências e intenção.
- Não traduzir citações protegidas sem licença válida para a tradução-alvo.
- Garantir que texto de thumbnail e título sejam concebidos para o idioma, não sobrepostos por máquina.
- Uma mudança no conteúdo canônico deve disparar revisão de todas as localizações afetadas.

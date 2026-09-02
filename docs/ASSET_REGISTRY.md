# Guia do asset registry

## Onde registrar

Os CSVs em `assets/registries/` são a lista operacional oficial. Eles começam apenas com cabeçalhos; isto **não** significa que algum asset foi aprovado.

### Campos de `asset_registry.csv`

| Campo | Preenchimento |
| --- | --- |
| `asset_id` | `ASSET-0001`, sequencial e único |
| `asset_type` | video, image, illustration, map, archive etc. |
| `name` | título/nome descritivo do item |
| `source_url` | URL específica do item e, se possível, URL de licença nas notas |
| `author` / `platform` | conforme informado pela origem |
| `license` | nome/versão exatos; não escrever só “livre” |
| `commercial_use_review` | yes / no / pending + racional nas notas |
| `attribution_required` | yes / no / unclear |
| `obtained_at_utc` | ISO 8601, por exemplo `2026-09-02` |
| `local_filename` / `sha256` | identificam a cópia usada |
| `content_id` / `scene_id` | relações de uso; separar múltiplas por `;` |
| `status` | candidate, approved, used, rejected, retired |
| `notes` | licença URL, restrições, créditos, versão etc. |

## Estados recomendados

- `candidate`: encontrado, sem avaliação concluída; não usar em edição final.
- `approved`: licença e adequação verificadas; disponível para uso.
- `used`: aparece no corte do vídeo; manter relação de cena e crédito.
- `rejected`: não usar; registrar motivo para não repetir pesquisa.
- `retired`: usado/registrado anteriormente, mas não selecionar para novos usos sem nova verificação.

## Auditoria de uma entrega

1. Liste todos os IDs presentes na timeline/EDL.
2. Confirme uma linha de registry para cada ID.
3. Confirme `approved` ou `used`, licença e URL verificáveis.
4. Compare arquivo local, hash e versão com a linha.
5. Gere créditos exigidos na descrição/metadados do vídeo.
6. Registre qualquer exceção como bloqueio de QA — nunca como nota informal.

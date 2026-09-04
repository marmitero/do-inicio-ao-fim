# Política de assets e licenças

## Regra de bloqueio

**Sem registro verificável, sem uso no corte final.** Um arquivo só pode ser usado após receber ID e linha no registry apropriado. A pessoa que seleciona o item é responsável por registrar a informação antes da edição final.

## Fontes permitidas sob verificação

Pexels, Pixabay, Wikimedia Commons, bibliotecas de áudio e bancos pagos podem ser considerados; o nome da plataforma não substitui a leitura da licença do item e de seus termos atuais. Cada asset precisa de fonte, URL, autor quando disponível, licença, data de obtenção e análise de uso comercial/atribuição.

## Campos e registros

- `assets/registries/asset_registry.csv`: fotos, vídeos, ilustrações e material de terceiros.
- `assets/registries/ai_asset_registry.csv`: mídia gerada por IA.
- `assets/registries/music_registry.csv`: faixas musicais.
- `assets/registries/sfx_registry.csv`: efeitos sonoros.

Cada ID é permanente. Não sobrescreva linha antiga para representar um novo download ou uma nova licença.

## Fluxo de avaliação

1. Localize o asset e abra a página/fonte da licença, não apenas resultado de busca.
2. Verifique uso comercial/YouTube, atribuição, modificações, redistribuição, restrições de IA, marcas/pessoas/propriedade e termos adicionais.
3. Salve localmente somente se necessário; registre data e URL de evidência.
4. Atribua ID e relações de conteúdo/cena antes de colocar na timeline.
5. Em QA, confirme que o arquivo usado corresponde ao ID e que os créditos exigidos constam de metadados/descrição.

## Red flags: escalar para decisão humana

- licença ausente, contraditória ou apenas “uso pessoal”;
- rosto, marca, obra de arte, edifício ou áudio com direitos não esclarecidos;
- asset marcado editorial-only;
- licença que conflita com monetização ou edição;
- obra bíblica/texto de tradução copiado de fonte de status desconhecido;
- termo de ferramenta de IA não claro sobre uso comercial;
- asset publicado em múltiplos lugares por autor não verificável.

## Assets de IA

Registrar ferramenta, versão/modelo quando disponível, data, prompt, imagem de referência usada, finalidade, restrições e cenas. Não usar referências protegidas ou rosto de pessoa real sem direito. IA serve como ilustração/reconstituição; não deve ser apresentada como registro histórico ou evidência arqueológica.

## Armazenamento

Binários de mídia são **versionados no Git** (ADR-019) para não se perderem entre sessões; apenas segredos e ruído de OS/ferramenta ficam fora. Os registros, URLs, hash/local filename e créditos também são versionados. O arquivo físico deve conservar nome que inclua o ID do registry quando possível.

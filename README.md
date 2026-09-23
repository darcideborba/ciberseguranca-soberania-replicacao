# Cibersegurança e soberania digital na digitalização dos serviços públicos

Pacote de dados e scripts de replicação da análise documental do arcabouço normativo federal brasileiro (2018-2026) sobre cibersegurança, soberania digital e governo digital.

*Replication package for a documentary analysis of the Brazilian federal regulatory framework (2018-2026) on cybersecurity, digital sovereignty and digital government.*

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `data/corpus_documental.csv` | Instrumentos do corpus codificado, instrumentos revogados usados na trajetória normativa, projeto de lei em tramitação e fontes dos casos ilustrativos, com emissor, data, URL oficial e situação no estudo (codificado, trajetória, em tramitação, caso ilustrativo). |
| `data/livro_de_codigos.csv` | Livro de códigos: oito dimensões de política (G, K, I, T, P, E, C, X), níveis de presença e graus de soberania (declarada, instrumentada). |
| `data/matriz_codificacao.csv` | Matriz final de codificação dos 17 instrumentos, com a trilha de política e os dispositivos que fundamentam cada atribuição. Valores: 2 = presença explícita; 1 = presença genérica; 0 = ausência; S = D, I, D/I ou 0. |
| `data/referencias_codificadas.ris` | Todas as referências do estudo em RIS (UTF-8), importáveis no Zotero, com a codificação registrada como etiquetas e os dispositivos em notas. |
| `scripts/contagens.py` | Recalcula os totais por dimensão a partir da matriz. |
| `scripts/gerar_ris.py` | Gera o arquivo RIS a partir dos metadados e da matriz. |

## Procedimento

- Corpus: instrumentos federais (leis, decretos, instruções normativas, resoluções e planos oficiais) editados ou vigentes entre jan. 2018 e set. 2026, que regulam ao menos uma das oito dimensões, com texto em fonte oficial. Busca realizada em setembro de 2026.
- Unidade de codificação: dispositivo (artigo, inciso ou item de plano).
- Codificação dedutiva independente por dois pesquisadores; concordância percentual de 87%; divergências resolvidas por consenso.

## Uso

```bash
python scripts/contagens.py
python scripts/gerar_ris.py
```

Requer Python 3.8 ou superior, sem dependências externas.

## Limitações conhecidas

- O conteúdo da IN GSI/PR n. 8/2025 foi verificado em fontes secundárias.
- A nota de esclarecimento do GSI sobre a IN n. 8/2025 teve sua existência confirmada, mas o conteúdo não pôde ser lido.

## Licença

Dados e documentação: CC BY 4.0. Scripts: MIT. Ver `LICENSE`.

## Como citar

Ver `CITATION.cff`. O DOI será atribuído pelo Zenodo na publicação da versão.

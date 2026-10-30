# Desafio 2 — Evoluindo a calculadora

## Organização

O desafio 1 concentra a leitura de números, as quatro operações, as mensagens de erro e o menu. O arquivo `desafio_02/calculadora.py` importa essas funções, preservando uma única implementação das operações básicas.

## Funcionalidade adicionada

A função `calcular(a, b, operacao)` da versão 2 verifica se a operação é `%`. Nesse caso, calcula `a * (b / 100)`: `a` é a base e `b` é a taxa. Para qualquer outra operação, chama a calculadora básica.

O menu compartilhado recebe `porcentagem=True` para mostrar a nova opção e usar os rótulos “Valor base” e “Porcentagem (%)”.

## Exemplos e testes de regressão

| Base | Taxa | Parcela percentual |
| ---: | ---: | ---: |
| 200 | 10 | 20 |
| 80 | 12,5 | 10 |
| 100 | 0 | 0 |
| 50 | 150 | 75 |

Para aplicar um desconto, subtraia a parcela da base: desconto de 10% em 200 resulta em `200 - 20 = 180`. A operação `%` isolada retorna `20`.

Os testes executam as quatro operações nas duas versões, além dos casos de porcentagem, entradas inválidas e divisão por zero. Assim, uma alteração que quebre uma operação anterior deve falhar na validação.

Execute `python -m desafio_02.calculadora` na raiz do repositório.

## Ferramenta usada

A evolução e a análise foram realizadas com assistência do Codex, não do Google Antigravity. Não há comprovação de execução no Antigravity.

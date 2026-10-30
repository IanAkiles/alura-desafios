# Desafio 1 — Entendendo a calculadora

## Principais componentes

- `ler_numero(texto)` converte o texto digitado em número e rejeita entradas inválidas, infinito e NaN.
- `calcular(a, b, operacao)` recebe dois números e o símbolo da operação. As condições `if`/`elif` escolhem a conta.
- `resultado_finito(numero)` verifica se a conta excedeu o limite numérico.
- `executar()` mostra o menu, recebe entradas e imprime resultados. O laço `while` permite repetir operações.
- `main()` inicia a versão básica. A condição `if __name__ == '__main__'` evita abrir o menu quando outro módulo importa as funções.

## Como entram os números e a operação?

`input()` sempre entrega texto. A variável `operacao` guarda um símbolo como `+`; `a` e `b` guardam números após conversão. A conversão aceita `2,5` e `2.5`. Não aceita separadores de milhar.

## Como a lógica realiza o cálculo?

Se a operação for `+`, a função devolve `a + b`. Os demais ramos aplicam subtração, multiplicação ou divisão. Antes de dividir, uma condição verifica se `b` é zero. Se ocorrer um erro de entrada, `try`/`except` apresenta uma mensagem e mantém o programa aberto.

## Experimentos reproduzíveis

| Operação | Primeiro número | Segundo número | Resultado esperado |
| --- | ---: | ---: | ---: |
| `+` | 2 | 3 | 5 |
| `-` | 2 | 5 | -3 |
| `*` | -4 | 3 | -12 |
| `/` | 7 | 2 | 3,5 |
| `/` | 5 | 0 | Erro de divisão por zero |

Use `python -m desafio_01.calculadora`, na raiz do repositório, para repetir os exemplos. Os testes também verificam essas operações.

## Ferramenta usada

Código desenvolvido com assistência do Codex. Não houve sessão no Google AI Studio. Esta explicação descreve o programa entregue; não é um relato de uso de uma ferramenta que não foi utilizada.

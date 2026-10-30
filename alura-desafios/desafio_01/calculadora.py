"""Calculadora de terminal com quatro operações básicas."""

import math


def ler_numero(texto: str) -> float:
    """Aceita vírgula ou ponto como separador decimal, sem separador de milhar."""
    try:
        numero = float(texto.strip().replace(',', '.'))
    except ValueError:
        raise ValueError('Digite um número válido, como 10 ou 2,5.') from None
    if not math.isfinite(numero):
        raise ValueError('Digite um número finito.')
    return numero


def resultado_finito(numero: float) -> float:
    if not math.isfinite(numero):
        raise ValueError('O resultado excede o limite numérico da calculadora.')
    return numero


def calcular(a: float, b: float, operacao: str) -> float:
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError('Use apenas números finitos.')
    if operacao == '+':
        resultado = a + b
    elif operacao == '-':
        resultado = a - b
    elif operacao == '*':
        resultado = a * b
    elif operacao == '/':
        if b == 0:
            raise ValueError('Não é possível dividir por zero.')
        resultado = a / b
    else:
        raise ValueError('Operação inválida.')
    return resultado_finito(resultado)


def executar(calculo=calcular, porcentagem=False):
    """Compartilha a interface de terminal entre os desafios 1 e 2."""
    menu = '+ somar | - subtrair | * multiplicar | / dividir'
    if porcentagem:
        menu += ' | % porcentagem (taxa sobre uma base)'
    print('Calculadora Python')
    print('Use ponto ou vírgula para decimais; não use separador de milhar.')
    while True:
        try:
            print('\n' + menu + ' | s sair')
            operacao = input('Operação: ').strip().lower()
            if operacao == 's':
                print('Até mais!')
                return
            if operacao not in ('+', '-', '*', '/') and not (porcentagem and operacao == '%'):
                print('Erro: operação inválida.')
                continue
            a = ler_numero(input('Valor base: ' if operacao == '%' else 'Primeiro número: '))
            b = ler_numero(input('Porcentagem (%): ' if operacao == '%' else 'Segundo número: '))
            print(f'Resultado: {calculo(a, b, operacao):.12g}')
        except ValueError as erro:
            print(f'Erro: {erro}')
        except (EOFError, KeyboardInterrupt):
            print('\nCalculadora encerrada.')
            return


def main():
    executar()


if __name__ == '__main__':
    main()

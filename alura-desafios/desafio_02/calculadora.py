"""Reutiliza a calculadora básica e acrescenta taxa sobre uma base."""

import math

from desafio_01.calculadora import calcular as calcular_basico
from desafio_01.calculadora import executar, resultado_finito


def calcular(a: float, b: float, operacao: str) -> float:
    if operacao != '%':
        return calcular_basico(a, b, operacao)
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError('Use apenas números finitos.')
    return resultado_finito(a * (b / 100))


def main():
    executar(calculo=calcular, porcentagem=True)


if __name__ == '__main__':
    main()

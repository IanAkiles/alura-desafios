import contextlib
import io
import unittest
from unittest.mock import patch

from desafio_01.calculadora import calcular, ler_numero, main
from desafio_02.calculadora import calcular as calcular_evoluida
from desafio_02.calculadora import main as main_evoluida


class CalculadorasTest(unittest.TestCase):
    def test_quatro_operacoes_nas_duas_versoes(self):
        for funcao in (calcular, calcular_evoluida):
            for operacao, a, b, esperado in (
                ('+', 2, 3, 5), ('-', 2, 5, -3),
                ('*', -4, 3, -12), ('/', 7, 2, 3.5),
                ('+', 0.1, 0.2, 0.3), ('*', 0, 9, 0),
            ):
                with self.subTest(funcao=funcao, operacao=operacao):
                    self.assertAlmostEqual(funcao(a, b, operacao), esperado)

    def test_divisao_zero(self):
        for funcao in (calcular, calcular_evoluida):
            with self.assertRaisesRegex(ValueError, 'zero'):
                funcao(5, 0, '/')

    def test_operacao_invalida(self):
        for funcao in (calcular, calcular_evoluida):
            with self.assertRaises(ValueError):
                funcao(2, 3, 'invalida')
        with self.assertRaises(ValueError):
            calcular(200, 10, '%')

    def test_leitura_aceita_ponto_virgula_e_negativo(self):
        for texto, esperado in [('1,5', 1.5), ('  -2.75 ', -2.75), ('0', 0)]:
            self.assertEqual(ler_numero(texto), esperado)

    def test_leitura_rejeita_entradas_invalidas(self):
        for texto in ['', 'abc', 'NaN', 'inf', '-Infinity', '1e999', '1,2.3']:
            with self.subTest(texto=texto), self.assertRaises(ValueError):
                ler_numero(texto)

    def test_calculo_rejeita_nao_finitos_e_estouro(self):
        for funcao in (calcular, calcular_evoluida):
            for a, b, op in [(float('nan'), 2, '+'), (1, float('inf'), '-'), (1e308, 1e308, '*')]:
                with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                    funcao(a, b, op)

    def test_porcentagem(self):
        for base, taxa, esperado in [(200, 10, 20), (80, 12.5, 10), (100, 0, 0), (-200, 10, -20), (50, 150, 75)]:
            with self.subTest(base=base, taxa=taxa):
                self.assertAlmostEqual(calcular_evoluida(base, taxa, '%'), esperado)

    def test_terminal_recupera_erro_e_continua(self):
        saida = io.StringIO()
        with patch('builtins.input', side_effect=['+', 'abc', '/', '4', '0', '+', '2,5', '3', 's']), contextlib.redirect_stdout(saida):
            main()
        self.assertIn('Erro:', saida.getvalue())
        self.assertIn('Resultado: 5.5', saida.getvalue())

    def test_terminal_porcentagem(self):
        saida = io.StringIO()
        with patch('builtins.input', side_effect=['%', '200', '10', 's']), contextlib.redirect_stdout(saida):
            main_evoluida()
        self.assertIn('Resultado: 20', saida.getvalue())

    def test_terminal_fim_de_entrada(self):
        with patch('builtins.input', side_effect=EOFError), contextlib.redirect_stdout(io.StringIO()):
            main()

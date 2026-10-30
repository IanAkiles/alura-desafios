import unittest

from desafio_03.modelo import ListaTarefas


class TarefasTest(unittest.TestCase):
    def setUp(self):
        self.lista = ListaTarefas()

    def test_adicionar_limpa_espacos(self):
        tarefa = self.lista.adicionar('  Estudar Python  ')
        self.assertEqual(tarefa.texto, 'Estudar Python')
        self.assertFalse(tarefa.concluida)
        self.assertEqual(self.lista.tarefas, [tarefa])

    def test_rejeita_vazia_e_muito_longa(self):
        for texto in ['', '   ', 'x' * 201]:
            with self.assertRaises(ValueError):
                self.lista.adicionar(texto)
        self.assertEqual(self.lista.tarefas, [])

    def test_tarefas_repetidas_tem_ids_diferentes(self):
        a = self.lista.adicionar('Estudar')
        b = self.lista.adicionar('Estudar')
        self.assertNotEqual(a.id, b.id)
        self.lista.remover(a.id)
        self.assertEqual(self.lista.tarefas, [b])

    def test_concluir_e_reabrir(self):
        t = self.lista.adicionar('Praticar')
        self.lista.alternar(t.id)
        self.assertTrue(t.concluida)
        self.lista.alternar(t.id)
        self.assertFalse(t.concluida)

    def test_id_inexistente(self):
        for metodo in (self.lista.alternar, self.lista.remover):
            with self.assertRaises(ValueError):
                metodo('inexistente')

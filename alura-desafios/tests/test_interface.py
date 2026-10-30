import tkinter as tk
import unittest

from desafio_03.app import App


class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.addCleanup(self.root.destroy)
        self.app = App(self.root)

    def test_adicionar_concluir_reabrir_remover(self):
        self.app.texto.set('Entregar os desafios')
        self.app.adicionar.invoke()
        ids = self.app.tabela.get_children()
        self.assertEqual(len(ids), 1)
        self.assertEqual(self.app.texto.get(), '')
        self.app.tabela.selection_set(ids[0])
        self.app.alternar.invoke()
        self.assertIn('concluida', self.app.tabela.item(ids[0], 'tags'))
        self.assertIn('1 concluída', self.app.resumo.get())
        self.app.alternar.invoke()
        self.assertIn('pendente', self.app.tabela.item(ids[0], 'tags'))
        self.app.remover.invoke()
        self.assertEqual(self.app.tabela.get_children(), ())

    def test_erros_sem_selecao_e_tarefa_vazia(self):
        self.app.alternar.invoke()
        self.assertIn('Selecione', self.app.mensagem.get())
        self.app.remover.invoke()
        self.assertIn('Selecione', self.app.mensagem.get())
        self.app.texto.set('  ')
        self.app.adicionar.invoke()
        self.assertIn('Informe', self.app.mensagem.get())
        self.assertEqual(self.app.tabela.get_children(), ())

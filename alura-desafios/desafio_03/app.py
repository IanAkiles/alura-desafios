"""Interface visual da lista de tarefas, construída com Tkinter."""

import tkinter as tk
from tkinter import font, ttk

from desafio_03.modelo import ListaTarefas


class App:
    def __init__(self, root):
        self.root = root
        self.modelo = ListaTarefas()
        self.texto = tk.StringVar(master=root)
        self.mensagem = tk.StringVar(master=root)
        self.resumo = tk.StringVar(master=root)
        root.title('Desafio 3 — Lista de tarefas')
        root.geometry('820x520')
        root.minsize(560, 380)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        painel = ttk.Frame(root, padding=20)
        painel.grid(sticky='nsew')
        painel.columnconfigure(0, weight=1)
        painel.rowconfigure(4, weight=1)
        ttk.Label(painel, text='Minha lista de tarefas', font=('Segoe UI', 19, 'bold')).grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 8))
        ttk.Label(painel, text='As tarefas ficam nesta sessão e são apagadas ao fechar.').grid(row=1, column=0, columnspan=2, sticky='w', pady=(0, 16))
        ttk.Label(painel, text='Nova tarefa (até 200 caracteres)').grid(row=2, column=0, sticky='w')
        self.entrada = ttk.Entry(painel, textvariable=self.texto)
        self.entrada.grid(row=3, column=0, sticky='ew', padx=(0, 8), pady=(4, 12))
        self.entrada.bind('<Return>', lambda event: self.acao('adicionar'))
        self.adicionar = ttk.Button(painel, text='Adicionar', command=lambda: self.acao('adicionar'))
        self.adicionar.grid(row=3, column=1, sticky='ew', pady=(4, 12))

        grade = ttk.Frame(painel)
        grade.grid(row=4, column=0, columnspan=2, sticky='nsew')
        grade.columnconfigure(0, weight=1)
        grade.rowconfigure(0, weight=1)
        self.tabela = ttk.Treeview(grade, columns=('texto', 'estado'), show='headings', selectmode='browse')
        self.tabela.heading('texto', text='Tarefa')
        self.tabela.heading('estado', text='Status')
        self.tabela.column('texto', width=540, minwidth=220)
        self.tabela.column('estado', width=110, minwidth=100, stretch=False)
        self.tabela.grid(row=0, column=0, sticky='nsew')
        barra = ttk.Scrollbar(grade, orient='vertical', command=self.tabela.yview)
        barra.grid(row=0, column=1, sticky='ns')
        self.tabela.configure(yscrollcommand=barra.set)
        self.fonte_concluida = font.nametofont('TkDefaultFont', root=root).copy()
        self.fonte_concluida.configure(overstrike=True)
        self.tabela.tag_configure('concluida', foreground='#385444', background='#e5f2e9', font=self.fonte_concluida)
        self.tabela.tag_configure('pendente', foreground='#19243b')

        botoes = ttk.Frame(painel)
        botoes.grid(row=5, column=0, columnspan=2, sticky='w', pady=12)
        self.alternar = ttk.Button(botoes, text='Concluir / reabrir', command=lambda: self.acao('alternar'))
        self.alternar.pack(side='left', padx=(0, 8))
        self.remover = ttk.Button(botoes, text='Remover selecionada', command=lambda: self.acao('remover'))
        self.remover.pack(side='left')
        ttk.Label(painel, textvariable=self.resumo).grid(row=6, column=0, columnspan=2, sticky='w')
        ttk.Label(painel, textvariable=self.mensagem, foreground='#a32332', wraplength=500).grid(row=7, column=0, columnspan=2, sticky='w', pady=(8, 0))
        self.render()
        self.entrada.focus_set()

    def acao(self, nome):
        try:
            if nome == 'adicionar':
                tarefa = self.modelo.adicionar(self.texto.get())
                selecionada = tarefa.id
                self.texto.set('')
            else:
                ids = self.tabela.selection()
                if not ids:
                    raise ValueError('Selecione uma tarefa primeiro.')
                selecionada = ids[0]
                if nome == 'alternar':
                    self.modelo.alternar(selecionada)
                elif nome == 'remover':
                    self.modelo.remover(selecionada)
            self.mensagem.set('')
            self.render(selecionada)
        except ValueError as erro:
            self.mensagem.set(str(erro))

    def render(self, selecionada=None):
        for id_tarefa in self.tabela.get_children():
            self.tabela.delete(id_tarefa)
        for tarefa in self.modelo.tarefas:
            estado = 'Concluída' if tarefa.concluida else 'Pendente'
            tag = 'concluida' if tarefa.concluida else 'pendente'
            self.tabela.insert('', 'end', iid=tarefa.id, values=(tarefa.texto, estado), tags=(tag,))
        if selecionada and self.tabela.exists(selecionada):
            self.tabela.selection_set(selecionada)
            self.tabela.see(selecionada)
        total = len(self.modelo.tarefas)
        concluidas = sum(t.concluida for t in self.modelo.tarefas)
        self.resumo.set(f'{total} tarefa(s) · {total - concluidas} pendente(s) · {concluidas} concluída(s)')


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()

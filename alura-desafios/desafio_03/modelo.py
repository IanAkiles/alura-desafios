"""Regras da lista, independentes da interface gráfica."""

from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Tarefa:
    id: str
    texto: str
    concluida: bool = False


class ListaTarefas:
    def __init__(self):
        self.tarefas: list[Tarefa] = []

    def adicionar(self, texto: str) -> Tarefa:
        texto = texto.strip()
        if not texto or len(texto) > 200:
            raise ValueError('Informe uma tarefa com 1 a 200 caracteres.')
        tarefa = Tarefa(id=uuid4().hex, texto=texto)
        self.tarefas.append(tarefa)
        return tarefa

    def buscar(self, id_tarefa: str) -> Tarefa:
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        raise ValueError('Tarefa não encontrada.')

    def alternar(self, id_tarefa: str):
        tarefa = self.buscar(id_tarefa)
        tarefa.concluida = not tarefa.concluida

    def remover(self, id_tarefa: str):
        self.tarefas.remove(self.buscar(id_tarefa))

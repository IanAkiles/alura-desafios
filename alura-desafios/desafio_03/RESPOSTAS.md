# Desafio 3 — Lista de tarefas visual

## Organização dos componentes

- `modelo.py`: define `Tarefa` e `ListaTarefas`. Cada tarefa possui ID, texto e indicação de conclusão.
- `app.py`: monta a janela Tkinter e liga os botões às ações do modelo.
- `tests/test_tarefas.py`: testa as regras sem depender da interface.
- `tests/test_interface.py`: cria widgets reais e verifica os botões, os estados e os contadores.

## Funcionalidades

**Adicionar:** lê o campo, remove espaços nas extremidades e valida o limite de 200 caracteres. O modelo gera um ID único. Duas tarefas com o mesmo texto continuam sendo registros distintos.

**Concluir:** altera o estado da tarefa selecionada. O mesmo botão permite reabrir uma tarefa concluída.

**Remover:** exclui a tarefa selecionada. Sem seleção, a interface mostra uma mensagem em vez de falhar.

## Melhoria visual

`render()` atualiza as linhas e aplica a tag `concluida` ou `pendente`. A tag `concluida` utiliza texto riscado, fundo verde e a coluna “Concluída”. A coluna informa o estado mesmo para quem não distingue as cores.

## Fluxo para experimentar

1. Execute `python -m desafio_03.app` na raiz do repositório.
2. Adicione “Estudar Python” e “Entregar os desafios”.
3. Selecione a primeira e clique em “Concluir / reabrir”.
4. Confira o texto riscado, o status e o contador.
5. Clique novamente para reabrir.
6. Remova uma tarefa e verifique a atualização da lista.

As tarefas são mantidas apenas enquanto a janela estiver aberta. O enunciado não exige salvamento em disco, e este projeto não o implementa.

## Ferramenta usada

Aplicação desenvolvida com assistência do Codex. Não foi executado um fluxo no Google Antigravity.

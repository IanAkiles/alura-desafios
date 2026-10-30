# Plano dos desafios

## Escopo
Implementar as três atividades descritas em alura.md. O usuário autorizou desenvolver com Codex e publicar um repositório público chamado alura-desafios. Não afirmar uso do Google AI Studio ou Antigravity.

## Estrutura e escolhas
- `desafio_01/calculadora.py`: quatro operações e entrada pelo terminal.
- `desafio_02/calculadora.py`: reutiliza a primeira calculadora e acrescenta porcentagem. Porcentagem significa calcular uma taxa sobre uma base: 10% de 200 = 20.
- `desafio_03/modelo.py` e `app.py`: lista de tarefas em memória, interface Tkinter, adicionar, concluir/reabrir e remover. Tarefas concluídas têm aparência distinta. Não há persistência exigida no enunciado.
- `tests/`: unittest, biblioteca padrão. Testes de funções, terminal e componentes reais do Tkinter.
- README e respostas por desafio: comandos, estrutura, explicações e limites.

Python 3.10 ou superior. Sem bibliotecas externas. As calculadoras usam float e não são indicadas para contabilidade.

## Execução
1. Escrever testes e confirmar falha pela ausência da implementação.
2. Implementar calculadoras, modelo e interface visual.
3. Executar testes, entradas reais de terminal e validação de sintaxe.
4. Revisar explicações, arquivos versionados e ausência de segredos.
5. Criar repositório público, enviar e conferir o commit remoto.

## Casos de validação
Divisão por zero; operação desconhecida; texto, vazio, NaN e infinito; estouro do resultado; números negativos e decimais; porcentagem; tarefa vazia; identificação de tarefas repetidas; ausência de seleção; reabertura e remoção; atualização visual e contadores.

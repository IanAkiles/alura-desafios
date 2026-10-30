# Alura — Desafios de programação com IA

Três atividades para praticar leitura, evolução e testes de software.

**Origem do desenvolvimento:** implementado com assistência do Codex. O enunciado menciona Google AI Studio e Google Antigravity, mas essas ferramentas não foram utilizadas nesta execução. A substituição foi autorizada pelo responsável pelo repositório. O código atende às funcionalidades propostas; a exigência de usar aquelas ferramentas deve ser conferida com o curso.

## Requisitos

- Python 3.10 ou superior.
- Tkinter para a interface do desafio 3. No instalador oficial do Python para Windows, mantenha o componente Tcl/Tk habilitado.
- Não é necessário instalar pacotes com pip.

## Executar

Abra um terminal na pasta raiz deste repositório. Execute um comando por vez:

```bash
python -m desafio_01.calculadora
python -m desafio_02.calculadora
python -m desafio_03.app
```

No Windows, se `python` não estiver disponível, use `py` no lugar de `python`.

| Pasta | Entrega |
| --- | --- |
| `desafio_01` | Calculadora de adição, subtração, multiplicação e divisão; respostas explicativas |
| `desafio_02` | Calculadora com porcentagem e reaproveitamento do desafio 1; explicação da evolução |
| `desafio_03` | Lista de tarefas visual com inclusão, conclusão, reabertura e remoção |
| `tests` | Testes das operações, do terminal, das tarefas e da interface |
| `docs` | Plano e registro da validação |

Mantenha as três pastas juntas. O desafio 2 importa a calculadora básica; os comandos acima resolvem os imports pela raiz do repositório.

## Como usar

**Calculadoras:** escolha `+`, `-`, `*` ou `/`, informe dois números e veja o resultado. Digite `s` para sair. Aceitam ponto ou vírgula decimal, sem separador de milhar. Entradas inválidas e divisão por zero mostram mensagem e retornam ao menu.

**Porcentagem:** na versão 2, escolha `%`, informe a base e a taxa. Base `200` e taxa `10` produzem `20`. A operação retorna a parcela percentual; não retorna automaticamente o total com desconto ou acréscimo.

**Lista visual:** digite uma tarefa e clique em **Adicionar** ou pressione Enter. Selecione uma linha para concluir/reabrir ou remover. As tarefas concluídas ficam riscadas, com fundo verde e status explícito. Os dados ficam em memória e são perdidos ao fechar a janela.

## Testar

```bash
python -m unittest discover -s tests -v
```

Os testes de interface criam widgets reais em janelas ocultas. Exigem uma sessão gráfica e Tcl/Tk funcional. Não são ignorados silenciosamente quando a interface está indisponível.

Para testar apenas as calculadoras e as regras da lista em um ambiente sem interface:

```bash
python -m unittest discover -s tests -p test_calculadoras.py -v
python -m unittest discover -s tests -p test_tarefas.py -v
```

## Limites

As calculadoras usam números de ponto flutuante e arredondam a apresentação para até 12 algarismos significativos. Pequenas diferenças de precisão são esperadas; não são sistemas contábeis. Não há avaliação de expressões com `eval`, acesso à rede, chaves de API ou serviços pagos.

Testes aprovados documentam os casos verificados, não uma garantia de ausência de qualquer erro. Veja [a validação](docs/validacao.md).

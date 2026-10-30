# Registro de validação

Data: 30/10/2026.

Ambiente: Windows, Python 3.11, biblioteca padrão e Tkinter.

## Resultado

Comando executado na raiz:

```text
python -m unittest discover -s tests -v
Ran 17 tests
OK
```

- 10 testes de calculadoras: quatro operações em ambas as versões, porcentagem, erros e fluxo de terminal.
- 5 testes do modelo de tarefas: inclusão, validação, IDs distintos, conclusão/reabertura e remoção.
- 2 testes da interface: botões reais, seleção, tags de conclusão, contadores e mensagens.

Na primeira execução, os testes da interface falharam porque o ambiente restrito impediu o carregamento do Tcl/Tk instalado. A mesma suíte, sem mudanças no código, passou ao executar com acesso ao ambiente gráfico local. Nenhum teste foi desabilitado.

Os testes foram escritos e executados antes da implementação: inicialmente falharam por ausência dos módulos. Após implementar, os 17 testes passaram.

## Limites da evidência

Não foram usados Google AI Studio ou Antigravity. Não foram verificados todos os sistemas operacionais, leitores de tela ou possíveis valores de entrada. Aprovação da suíte não significa garantia de zero defeitos.

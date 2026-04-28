# Depuração de debug.py

## Erros encontrados e correções aplicadas

1. `item1 = float(input(Preço do item 1? ))`
   - Erro: a string do prompt não estava entre aspas.
   - Correção: `item1 = float(input("Preço do item 1? "))`

2. `print(" Item 2:        R$ {total_item2:.2f}")`
   - Erro: faltava `f` antes da string, então o placeholder não era formatado.
   - Correção: `print(f" Item 2:        R$ {total_item2:.2f}")`

3. `desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))`
   - Erro: o valor do cupom era lido como string e depois comparado a número e usado em cálculo.
   - Correção: converter para `float` imediatamente: `desconto_cupom = float(input(...))`

4. `if desconto_cupom > 0:` seguido por `print(...)`
   - Erro: a instrução `print` estava sem indentação, causando erro de sintaxe no bloco `if`.
   - Correção: identar o `print` com quatro espaços.

## Observações adicionais

- `subtotal`, `imposto` e `desconto` agora são calculados corretamente com valores numéricos.
- O uso de f-strings garante que os valores sejam exibidos formatados com duas casas decimais.
- A mensagem de total final foi mantida com formato adequado.

## Código corrigido

O arquivo `debug.py` foi ajustado para:
- ler corretamente os prompts de entrada;
- converter valores para `int` e `float` nas entradas;
- usar `f-strings` nas saídas;
- verificar o desconto corretamente e imprimir apenas quando houver cupom.

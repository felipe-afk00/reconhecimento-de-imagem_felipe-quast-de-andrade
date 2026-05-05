# CÓDIGO CORRIGIDO

# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))  # converte para inteiro porque quantidade deve ser número inteiro
item1 = float(input("Preço do item 1? "))  # usa float para aceitar valores decimais de preço

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1  # calcula o valor total do primeiro item
total_item2 = qtd2 * item2  # calcula o valor total do segundo item
total_item3 = qtd3 * item3  # calcula o valor total do terceiro item

subtotal = total_item1 + total_item2 + total_item3  # soma os valores totais antes de aplicar impostos e descontos
imposto = subtotal * 0.10  # aplica alíquota fixa de 10% ao subtotal

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)  # converte percentual em valor monetário

# TOTAL FINAL
total = subtotal + imposto - desconto  # adiciona imposto e subtrai desconto do total

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
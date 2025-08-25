# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = reais / taxa_dolar
valor_euro = reais / taxa_euro
print(f"Valor em Reais: R$ {reais}\nValor em Dólares: $ {valor_dolar:.2f}\nValor em Euros: € {valor_euro:.2f}")
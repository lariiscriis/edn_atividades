# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 0.20

valor_de_desconto = preco_original * porcentagem_desconto
preco_final = preco_original - valor_de_desconto

print(f"Produto: {nome_produto}\nPreço Original: R$ {preco_original}\nPorcentagem de Desconto: 20%\nValor do Desconto: R${valor_de_desconto}\nPreço Final: R${preco_final}")
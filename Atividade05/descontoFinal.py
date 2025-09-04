# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.


def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

preco_produto = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (ex: 20 para 20%): "))
preco_com_desconto = calcular_desconto(preco_produto, percentual_desconto)
print(f"O preço final após o desconto é: R$ {preco_com_desconto}")

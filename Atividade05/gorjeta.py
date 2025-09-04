# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta 
# e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e
# na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta*(porcentagem_gorjeta/100)

    return round(gorjeta,2)


total_conta = float(input("Digite o valor total da conta: R$ "))
percentual_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

gorjeta = calcular_gorjeta(total_conta, percentual_gorjeta)

print(f"A gorjeta sugerida é: R$ {gorjeta}")
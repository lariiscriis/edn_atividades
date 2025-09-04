# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime


def calcular_idade_em_dias(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    data_atual = datetime.now()
    idade_em_dias = (data_atual - data_nascimento).days
    return idade_em_dias

data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
idade_dias = calcular_idade_em_dias(data_nascimento)
print(f"Você está vivo há {idade_dias} dias.")

# 3 - Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import pandas as pd

def ler_dados_csv(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        return df
    except FileNotFoundError:
        return "Arquivo não encontrado."
nome_arquivo = input("Digite o nome do arquivo csv: ")
print(ler_dados_csv(nome_arquivo))


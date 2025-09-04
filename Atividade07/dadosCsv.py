# 2 - Crie um script em Python que escreva dados em um arquivo CSV. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import pandas as pd

def escrever_dados_csv(nome_arquivo, dados):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)
    print(f"Dados escritos no arquivo {nome_arquivo} com sucesso.")
nome_arquivo = "pessoas.csv"
dados = [
    {"Nome": "Ana", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 34, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"},
]
escrever_dados_csv(nome_arquivo, dados)
print("Conteúdo do arquivo CSV:")
df = pd.read_csv(nome_arquivo)
print(df)

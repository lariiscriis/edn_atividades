# 4 -Crie um script em Python que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import json
def escrever_dados_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    print(f"Dados escritos no arquivo {nome_arquivo} com sucesso.")
def ler_dados_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return "Arquivo não encontrado."
nome_arquivo = "pessoa.json"
dados = {
    "nome": "Larissa",
    "idade": 19,
    "cidade": "Praia Grande"
}
escrever_dados_json(nome_arquivo, dados)
print("Conteúdo do arquivo JSON:")
print(ler_dados_json(nome_arquivo))

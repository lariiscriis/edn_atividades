# 3 - Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
# utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado. 

import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if 'erro' in dados:
        return None
    return dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']
cep_input = input("Digite o CEP (somente números): ")
resultado = consultar_cep(cep_input)
if resultado:
    logradouro, bairro, cidade, estado = resultado
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
else:
    print("CEP não encontrado ou inválido.")
    
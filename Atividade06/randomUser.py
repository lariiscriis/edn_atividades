# 2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
# O programa deve exibir o nome, email e país do usuário gerado.

import requests
def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    dados = resposta.json()
    
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    return nome, email, pais

nome, email, pais = gerar_usuario_aleatorio()
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"País: {pais}")




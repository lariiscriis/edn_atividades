# 4 - Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
# O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
# máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter 
# os dados de cotação.


import requests
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if f"{moeda}BRL" not in dados:
        return None
    cotacao_info = dados[f"{moeda}BRL"]
    valor_atual = cotacao_info['bid']
    valor_maximo = cotacao_info['high']
    valor_minimo = cotacao_info['low']
    data_hora = cotacao_info['create_date']
    
    return valor_atual, valor_maximo, valor_minimo, data_hora
moeda_input = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
resultado = consultar_cotacao(moeda_input)
if resultado:
    valor_atual, valor_maximo, valor_minimo, data_hora = resultado
    print(f"Cotação atual de {moeda_input} em BRL:")
    print(f"Valor Atual: R$ {valor_atual}")
    print(f"Valor Máximo: R$ {valor_maximo}")
    print(f"Valor Mínimo: R$ {valor_minimo}")
    print(f"Data e Hora da Última Atualização: {data_hora}")
else:
    print("Moeda inválida ou não encontrada.")
    
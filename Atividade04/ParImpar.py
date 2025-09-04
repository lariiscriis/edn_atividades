# 4 - Criar um código que serve para analisar números digitados pelo usuário, 
# classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

pares = 0
impares = 0

while True:
    try:
        entrada = input("Digite um número inteiro ou 'fim' para sair:")

        if entrada.lower() == 'fim':
            break

        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par")
            pares += 1
        else:
            print(f"{numero} é ímpar")
            impares += 1

    except ValueError:
        print("Erro: o valor digitado não é um número inteiro válido. Tente novamente.")

print(f"Números pares digitados: {pares}")
print(f"Números ímpares digitados: {impares}")
print("Programa encerrado.")
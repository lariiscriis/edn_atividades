# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

idade = int(input("Olá!\nDigite a sua idade: "))

if idade < 0:
    print("Você não pode ter idade negativa.")
elif idade <= 12:
    print("Criança. ")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
    
print("Fim do programa")
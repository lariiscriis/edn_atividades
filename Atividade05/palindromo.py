# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def eh_palindromo(texto):
    texto = ''.join(caractere.lower() for caractere in texto if caractere.isalnum())
    return texto == texto[::-1] 
entrada = input("Digite uma palavra ou frase: ")

if eh_palindromo(entrada):
    print("Sim")
else:
    print("Não")
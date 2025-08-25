# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
    

ano_calc = int(input("Digite um ano: "))

if ano_calc % 4 == 0:
    if ano_calc % 100 == 0:
        if ano_calc % 400 == 0:
            print (f"{ano_calc} é bissexto")
        else:
            print(f"{ano_calc} não é bissexto")
    else:
        print(f"{ano_calc} é bissexto")    
else:
    print(f"{ano_calc} não é bissexto")
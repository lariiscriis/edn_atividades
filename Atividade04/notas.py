# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

notas = []

while True:
    try:
        entrada = input("Digite as notas entre 0 e 10 ou 'fim' para encerrar o programa: ")
        
        if entrada.lower() == 'fim':
            break
        
        nota = float(entrada)
        
        if nota < 0 or nota > 10:
             raise Exception()
        
        notas.append(nota)
        

    except ValueError:
        print("Erro: entrada inválida. Insira um número entre 0 e 10 ou 'fim' para encerrar.")
    except Exception:
        print("Erro: nota fora do intervalo permitido. Insira um número entre 0 e 10.")

soma = 0
if len(notas) > 0:
    for nota in notas:
        soma += nota

    media = soma / len(notas)
    print("A média é:", media)

else:
     print("Nenhuma nota foi registrada.")
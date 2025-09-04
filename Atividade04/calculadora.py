# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = numero1 + numero2
        elif operacao == '-':
            resultado = numero1 - numero2
        elif operacao == '*':
            resultado = numero1 * numero2
        elif operacao == '/':
            if numero2 == 0:
                print("Dvisão por zero não é permitida. Tente novamente.")
                continue
            resultado = numero1 / numero2
        else:
            raise Exception()
        print(f"Resultado: {resultado}")
        break
        
    except ValueError:
        print("Entrada inválida. Insira números válidos.")
    except ZeroDivisionError:
        print("Divisão por zero não é permitida. Tente novamente.")
    except Exception:
        print("Operação inválida. Tente novamente.")
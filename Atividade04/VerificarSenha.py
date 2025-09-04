# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.


while True:
    try:
        senha = input("Digite a senha ser verificada ou fim para encerrar o programa: ")

        if senha.lower() == 'fim':
            print("Programa encerrado.")
            break

        if len(senha) < 8:
            raise Exception("A senha deve ter pelo menos 8 caracteres.")
        
        tem_numero = False
        for caractere in senha:
            if caractere in '0123456789':
                tem_numero = True
                break

        if tem_numero == False:
            raise Exception("Sua senha deve conter pelo menos um número.")

        print("Senha válida.")
        break

    except Exception as e:
        print(f"{e} Tente novamente.")

        

# 10 Faça um programa que receba uma senha formada de quatro números inteiros,
# verifique se a senha está correta e, caso não esteja, solicite novamente a senha.
# Se a senha de entrada for a correta, deverá ser apresentada a mensagem “Senha Correta”,
# caso contrário, “Senha Incorreta”.


senha_cadastrada = input('\nCadastre uma senha de 4 dígitos: ')

while True:

    if len(senha_cadastrada) != 4:

        senha_cadastrada = input('\nSenha inválida! Cadastre uma senha de 4 dígitos: ')

    else:
        break

while True:

    print(f'\n{"=" * 25}')
    print(f'{" " * 10}LOGIN{" " * 10}')
    print(f'{"=" * 25}')

    senha = input('\nDigite sua senha: ')

    if senha == senha_cadastrada:

        print('\nSenha Correta!')
        break

    else:

        print('\nSenha Incorreta!')

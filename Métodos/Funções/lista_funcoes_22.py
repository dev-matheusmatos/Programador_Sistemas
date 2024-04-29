from random import randint


def menu():
    print('''=============JOKENPO==============
[1] PEDRA 
[2] PAPEL 
[3] TESOURA    

    ''')


def validar_jogada(jogada):0
    if 1 <= int(jogada) <= 3:
        return True
    return False


def jogar_p2():
    return randint(1, 3)


def definir_vencedor(jogada_p1, jogada_p2):
    if jogada_p2 == jogada_p1:
        return 'Empate'
    elif (jogada_p1 == 1 and jogada_p2 == 3 or
            jogada_p1 == 2 and jogada_p2 == 1 or
            jogada_p1 == 3 and jogada_p2 == 2):
        return 'Vitória P1'
    else:
        return 'Vitória P2'


menu()
jogada_p1 = input('Escolha: ')
if validar_jogada(jogada_p1):
    jogada_p2 = jogar_p2()
    print('Escolha PC:',jogada_p2)
    print(definir_vencedor(int(jogada_p1), jogada_p2))
else:
    print('Jogada inválida')
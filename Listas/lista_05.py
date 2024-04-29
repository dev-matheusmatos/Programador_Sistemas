from lista_05_imports import logo_hemosc, menu
from datetime import datetime

tipos_sangue = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
estoque_bolsas = [0, 0, 0, 0, 0, 0, 0, 0]
movimentacoes = []
data_hoje = datetime.now().strftime("%Y-%m-%d %H:%M")

while True:
    print(logo_hemosc)
    print(data_hoje)
    print(menu)

    opcao = int(input('Opção: '))

    if opcao == 1:
        nome = input('Nome do doador: ')
        idade = int(input('Idade do doador: '))
        tipo_sanguineo_doador = input('Tipo sanguíneo: ')

        if 18 <= idade <= 65:
            if tipo_sanguineo_doador in tipos_sangue:
                estoque_bolsas[tipos_sangue.index(tipo_sanguineo_doador)] += 1
                movimentacoes.append([nome, idade, tipo_sanguineo_doador, data_hoje])

            else:
                print('Tipo de sangue inválido!')

        else:
            print('Para doar, precisa ter entre 18 e 65 anos!')

    elif opcao == 2:
        pass

    elif opcao == 3:
        for i in range(8):
            print(tipos_sangue[i], estoque_bolsas[i])

    elif opcao == 4:
        for i in movimentacoes:
            print(i)

    elif opcao == 5:
        break

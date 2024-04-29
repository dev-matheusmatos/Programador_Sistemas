taxas_juros = {'A': 0.02,
               'B': 0.05,
               'C': 0.1,
               'D': 0.12,
               'E': 0.14}

valor = float(input('Qual valor: '))
taxa = input('Qual taxa: [A] [B] [C] [D] [E]: ').upper()

if taxa not in taxas_juros:
    print('Não existe esta taxa!')

else:
    print(f'Valor Final: {valor * (1 + taxas_juros[taxa]):.2f}')

    
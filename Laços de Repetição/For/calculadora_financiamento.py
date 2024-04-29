print('\nCalculadora de Amortização: Price e SAC')

valor_presente = float(input('\nValor Presente: '))
taxa_juros_mensal = float(input('Taxa de Juros Mensal (%): '))
numero_meses = int(input('N° Meses: '))

print()

saldo_devedor = valor_presente

print(f'{"-"*36}PRICE{"-"*36}')
print()
print('Nº: '.center(15), end='')
print('Valor da Parcela: '.center(15), end='')
print('Amortização: '.center(15), end='')
print('Juros: '.center(15), end='')
print('Saldo Devedor: '.center(15))

valor_parcela = (valor_presente * (taxa_juros_mensal / 100)) / (1 - (1 + (taxa_juros_mensal / 100)) ** -(numero_meses))

for i in range(1, numero_meses + 1):

    juros = saldo_devedor * (taxa_juros_mensal / 100)
    amortizacao = valor_parcela - juros
    saldo_devedor -= amortizacao

    print(str(i).center(15), end='')
    print(str(round(valor_parcela, 2)).center(15), end='')
    print(str(round(amortizacao, 2)).center(15), end='')
    print(str(round(juros, 2)).center(15), end='')
    print(str(round(saldo_devedor, 2)).center(15))

print('\n'*3)

print(f'{"-"*36}SAC{"-"*36}')
print()
print('Nº: '.center(15), end='')
print('Valor da Parcela: '.center(15), end='')
print('Amortização: '.center(15), end='')
print('Juros: '.center(15), end='')
print('Saldo Devedor: '.center(15))

saldo_devedor = valor_presente
amortizacao = valor_presente / numero_meses

for i in range(1, numero_meses + 1):

    juros = saldo_devedor * (taxa_juros_mensal / 100)
    valor_parcela = amortizacao + juros
    saldo_devedor -= amortizacao
    print(str(i).center(15), end='')
    print(str(round(valor_parcela, 2)).center(15), end='')
    print(str(round(amortizacao, 2)).center(15), end='')
    print(str(round(juros, 2)).center(15), end='')
    print(str(round(saldo_devedor, 2)).center(15))
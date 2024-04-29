# 0 1 . 2 3 4 . 5 6 7 / 8 9 10 11 - 12 13
print('\n========================================')
print('           VALIDADOR DE CNPJ')
print('========================================')
cnpj = input('\nInforme o CNPJ (apenas dígitos): ')

mult_01 = 6
mult_02 = 2

soma = 0

for digito in cnpj[:12]:

    if mult_01 < 10:

        soma += mult_01 * int(digito)
        mult_01 += 1

    else:

        soma += mult_02 * int(digito)
        mult_02 += 1


digito_1 = soma % 11

if digito_1 > 9:
    digito_1 = 0

soma = 0
mult_01 = 5
mult_02 = 2

for digito in cnpj[:13]:

    if mult_01 < 10:

        soma += mult_01 * int(digito)
        mult_01 += 1

    else:

        soma += mult_02 * int(digito)
        mult_02 += 1

digito_2 = soma % 11

if digito_2 > 9:
    digito_2 = 0

if digito_1 == int(cnpj[-2]) and digito_2 == int(cnpj[-1]):
    print(f'\nO CNPJ {cnpj} informado é válido!')

else:
    print(f'\nO CNPJ {cnpj} informado NÃO é válido!')



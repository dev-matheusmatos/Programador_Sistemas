print(f'\n{"=" * 38}')
print(f'{" " * 10}Verificador de CPF{" " * 10}')
print(f'{"=" * 38}')
print()

cpf = input('Informe o CPF (apenas dígitos): ')
print()

soma = 0
mult = 10

for digito in cpf[:9]:

    soma += mult * int(digito)
    mult -= 1

digito_01 = 11 - (soma % 11)

if digito_01 > 9:
    digito_01 = 0

soma = 0
mult = 11

for digito in cpf[:10]:

    soma += mult * int(digito)
    mult -= 1

digito_02 = 11 - (soma % 11)

if digito_02 > 9:
    digito_02 = 0

if digito_01 == int(cpf[-2]) and digito_02 == int(cpf[-1]):
    print(f'O CPF {cpf} informado é VÁLIDO!')

else:
    print(f'O CPF {cpf} informado NÃO é válido!')


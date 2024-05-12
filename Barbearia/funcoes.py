def validar_cpf(cpf):
    num_cpf = ''
    for digito in cpf:
        if digito in '0123456789':
            num_cpf += digito

    mult = 10
    soma = 0
    digito_01 = 0
    digito_02 = 0

    for i in range(9):
        soma += int(num_cpf[i]) * mult
        mult -= 1

    resto = 11 - (soma % 11)

    if resto == 10 or resto == 11:
        digito_01 = 0
    else:
        digito_01 = resto

    soma = 0
    mult = 11

    for i in range(10):
        soma += int(num_cpf[i]) * mult
        mult -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito_02 = 0
    else:
        digito_02 = resto

    if digito_01 == int(num_cpf[9]) and digito_02 == int(num_cpf[10]):
        return True
    return False

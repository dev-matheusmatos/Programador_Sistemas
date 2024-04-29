# função

def somar(n1, n2):
    return n1 + n2


def multiplicar(n1, n2):
    return n1 * n2


def comeca_com_vogal(texto):
    if str(texto[0]).lower() in 'aeiouáéíóúãâôê':
        return True
    return False


print(comeca_com_vogal('Ágatha'))
print(somar(5, 8))
print(multiplicar(5, 8))


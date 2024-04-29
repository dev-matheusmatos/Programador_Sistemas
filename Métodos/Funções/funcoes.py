# criar uma função que retorna True or False para um número par

def is_even(number):
    if number % 2 == 0:
        return True
    return False


# def eh_palindromo(texto):
#
#     novo_texto = ''
#     for i in range(len(texto) - 1, -1, -1):
#         novo_texto += texto[i]
#
#     if novo_texto == texto:
#         return True
#     return False


def eh_palidromo(texto):
    if texto.lower() == texto[::-1].lower():
        return True
    return False



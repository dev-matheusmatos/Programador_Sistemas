# 11 Escreva uma função que inverta uma string (por exemplo, "python"
# se tornaria "nohtyp").

def inverter_texto(texto):
    return texto[::-1]


# 12 Crie uma função que verifique se uma palavra é um palíndromo
# (ou seja, pode ser lida da mesma forma de trás para frente).
#
# Ex: MUSUM, OVO…

def eh_palidromo(texto):
    if texto.lower() == texto[::-1].lower():
        return True
    return False


# 13 Implemente uma função que receba uma lista de números e retorne
# uma nova lista contendo apenas os números pares.

def informar_pares(lista_numeros):
    lista_pares = []
    for i in lista_numeros:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares


# 14 Escreva uma função que receba uma lista de strings e retorne uma
# nova lista com todas as palavras em maiúsculas.

def informar_palavras_maiusculas(lista_textos):
    lista_maiusculas = []
    for i in lista_textos:
        if i.isupper():
            lista_maiusculas.append(i)
    return lista_maiusculas


# 15 Crie uma função que calcule a potência de um número
# (por exemplo, 2^3 = 8).

def calcular_potencia(numero, expoente):
    return numero ** expoente









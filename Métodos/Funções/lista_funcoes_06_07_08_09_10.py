# 06 Crie uma função que verifique se um número é par ou ímpar e
# retorne "Par" ou "Ímpar" de acordo.

def eh_par(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'

# 07 Implemente uma função que receba uma lista de números e retorne o
# maior valor.


def maior(lista_numeros):
    return max(lista_numeros)


# 08 Escreva uma função que receba uma lista de números e retorne a
# média deles.

def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


# 09 Crie uma função que receba uma string como argumento e retorne o
# número de vogais nela.

def contar_vogais(texto):
    vogais = 0
    for i in texto.lower():
        if i in 'aeiouáéíóúãõâêôü':
            vogais += 1
    return vogais


# 10 Implemente uma função que receba uma lista de palavras e retorne
# a palavra mais longa.

def verificar_maior_palavra(lista_palavras):
    lista_maior_palavra = [lista_palavras[0]]
    for i in lista_palavras[1:]:
        if len(i) == len(lista_maior_palavra[0]):
            lista_maior_palavra.append(i)
        elif len(i) > len(lista_maior_palavra[0]):
            lista_maior_palavra.clear()
            lista_maior_palavra.append(i)
    return lista_maior_palavra


print(verificar_maior_palavra(['Abacaxi', 'Ebecexi', 'toranja', 'Obocoxi']))


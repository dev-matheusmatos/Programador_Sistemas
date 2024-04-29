# 01 Crie uma função que permita contar o número de vezes que aparece
# uma letra em uma string.

def contar_letra(texto, letra):
    quantidade = 0
    for caractere in texto:
        if caractere == letra:
            quantidade += 1
    return quantidade

# 02 Faça uma função que retorne o reverso de um número inteiro
# informado.
# Por exemplo: 127 -> 721.


def inverter_num_inteiro(numero):
    return int(str(numero[::-1]))


# 03 Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado

def verificar_qnt_digitos(numero):
    return len(str(numero))


# 04 Crie uma função que receba dois números como argumentos e retorne
# sua soma.

def somar(n1, n2):
    return n1 + n2


# 05 Escreva uma função que calcule o fatorial de um número inteiro
# positivo.

def calcular_fatorial(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    return fatorial


# 16 Implemente uma função que receba uma lista de números e retorne a
# soma de todos os números ímpares.

def somar_numeros_impares(lista_numeros):
    lista_impares = []
    for i in lista_numeros:
        if i % 2 != 0:
            lista_impares.append(i)
    return sum(lista_impares)


# 17 Escreva uma função que converta uma temperatura em graus Celsius
# para Fahrenheit.

def converter_celsius_fah(temperatura):
    return (temperatura * 1.8) + 32


# 18 Crie uma função que calcule o número de dias em um número de anos
# fornecido como argumento (levando em consideração anos bissextos).

def calcular_dias(anos):
    dias = 365 * anos
    if anos >= 4:
        dias += anos // 4
    return dias


# 19 Implemente uma função que receba uma lista de números e retorne
# uma nova lista com os números em ordem crescente.

def ordernar_crescente(lista_numeros):
    lista_numeros.sort()
    return lista_numeros


# 20 Crie uma função que determine se um número é primo ou não e
# retorne True ou False.

def verificar_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True



import re


def verificar_placa(placa):
    """
    Verifica se a placa fornecida é válida segundo os padrões brasileiros.

    Padrões aceitos:
    - Antigo: ABC-1234
    - Novo: ABC1D23

    :param placa: str, placa a ser verificada
    :return: bool, True se a placa for válida, False caso contrário
    """
    # Regex para o formato antigo (ABC-1234)
    padrao_antigo = re.compile(r'^[A-Z]{3}-\d{4}$')

    # Regex para o novo formato (ABC1D23)
    padrao_novo = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')

    # Verifica se a placa corresponde a algum dos padrões
    if padrao_antigo.match(placa) or padrao_novo.match(placa):
        return True
    return False


# Exemplos de uso
placas = ["ABC-1234", "XYZ1A23", "AAA-0000", "BBB2C45", "123-ABCD"]
for placa in placas:
    if verificar_placa(placa):
        print(f"A placa {placa} é válida.")
    else:
        print(f"A placa {placa} é inválida.")

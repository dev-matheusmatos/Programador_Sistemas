# operational system

import os

path = r'C:\Users\Matheus Matos\Desktop\Estudos\Jovem Progamador\Programador_Sistemas\Bibliotecas'
for arquivo in os.listdir(path):
    if arquivo.endswith('.py'):
        print(arquivo)

    else:
        os.remove(rf'{path}\{arquivo}')
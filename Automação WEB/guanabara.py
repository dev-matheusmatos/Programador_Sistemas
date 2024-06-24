from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://www.youtube.com/c/CursoemV%C3%ADdeo/playlists'
browser = Edge()
browser.get(url)
lista_titulos = []
final = False
while True:
    print('-------------------------')
    browser.execute_script("window.scrollTo(0, 5000);")
    sleep(2)
    titulos = browser.find_elements(By.ID, 'video-title')
    for titulo in titulos[::-1]:
        if titulo.text in lista_titulos:
            final = True
            break
        lista_titulos.append(titulo.text)
    if final:
        break

for i, titulo in enumerate(lista_titulos):
    print(f'{i+1} - {titulo}')
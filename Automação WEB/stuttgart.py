from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = 'https://www.stuttgart.com.br/bomboniere/barras-de-chocolate.html'
browser = Edge()
browser.get(url)

lista_produtos = []
final = False
while True:
    browser.execute_script("window.scrollTo(0, 5000);")
    sleep(2)
    produtos = browser.find_elements(By.CSS_SELECTOR, '#layer-product-list .product-item-link')
    for produto in produtos[::-1]:
        if produto.text in lista_produtos:
            final = True
            break
        lista_produtos.append(produto.text)
    if final:
        break

for i, produto in enumerate(lista_produtos):
    print(f'{i+1} - {produto}')


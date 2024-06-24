from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://www.youtube.com/c/CursoemV%C3%ADdeo/playlists'

# Inicializar o WebDriver para o Edge
browser = Edge()

# Abrir a página desejada
browser.get(url)
sleep(6)

# Função para scrollar até o fim da página
def scroll_to_end(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        # Scrollar para o fim da página
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        sleep(3)  # Esperar para o novo conteúdo carregar

        # Calcular a nova altura da página e comparar com a última altura
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Scrollar até o fim da página
scroll_to_end(browser)

# Encontrar os elementos dos títulos dos vídeos
titulos = browser.find_elements(By.ID, 'video-title')

# Imprimir os títulos dos vídeos
for titulo in titulos:
    print(titulo.text)

# Fechar o navegador
browser.quit()

# selenium

# definir o navegador
# instalar o webdriver
# instalar o selenium

from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys

browser = Edge()

browser.get('https://www.google.com.br')
browser.find_element('name', 'q').send_keys('jonas gameplays', Keys.ENTER)

input()
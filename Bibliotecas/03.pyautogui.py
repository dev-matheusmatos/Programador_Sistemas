import pyautogui as pg
from time import sleep

pg.press('win')
pg.write('paint')
pg.press('Enter')
sleep(1)
# clicar para gerar círculo
pg.click(621,113)
pg.click(621,113)
# clicar para abrir opção cor sólida
pg.click(824,165)
sleep(0.5)
# clicar para selecionar cor sólida
pg.click(795,280)
pg.click(795,280)

# selecionar vermelho
pg.click(1159,113)
pg.click(1159,113)
# selecionar segunda opção vermelho
pg.click(1018,169)
pg.click(1018,169)
pg.click(1159,113)
pg.click(1159,113)

# fazer círculo
pg.click(694,345)
pg.click(694,345)
pg.dragTo(1194,839)
pg.click(1194,869)

# fechar tela
pg.click(1884,10)

# selecionar salvar
sleep(0.3)
pg.click(842,590)
sleep(0.3)
pg.write('Pais que levou bomba kabuuum')
# selecionar disco c
pg.click(952,377)
pg.click(952,377)
pg.click(1339,726)
pg.click(1045,550)
pg.click(1339,726)
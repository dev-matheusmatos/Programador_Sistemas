# pyautogui

import pyautogui as pg
from time import sleep
# pg.click(1870, 1050)

pg.press('win')
pg.write('calculadora')
pg.press('Enter')
sleep(1)
pg.write('7*2')
pg.press('ENTER')

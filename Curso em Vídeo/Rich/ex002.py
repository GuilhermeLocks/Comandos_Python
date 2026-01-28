from rich import print
from rich.panel import Panel
import os
from time import sleep

caixa = Panel('Esse aqui é um painel de exemplo', title=' mensage', style='red')
caixa_2 = Panel('Esse aqui é um segundo painel de exemplo', title=' mensage', style='red')

print('caixa')
sleep(2)
os.system('cls')
print('caixa_2')
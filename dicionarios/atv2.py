#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


import random
jogador1 = input("digite seu nome: ")
jogador2 = input("digite seu nome: ")
jogador3 = input("digite seu nome; ")
jogador4 = input("digite sue nome:")

import time


jogadores = {}

print(f"jogadores, jogando dados... ") 
time.sleep(5)

jogadores[jogador1] = random.randint(1,6)
jogadores[jogador2] = random.randint(1,6)
jogadores[jogador3] = random.randint(1,6)
jogadores[jogador4] = random.randint(1,6)


for k, v in jogadores.items():

    print(f" o resultado do dado do jogador {k} foi {v}")
print(jogadores)
for i in sorted(jogadores, key = jogadores.get):
    print(i,jogadores[i])
#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random


num = (random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11),random.randint(1,11))
print('os numeros sorteados foram',num)
maior = 0
menor = 11111110100010101011001010110101101010111111111111010101010101
for n in num:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(" o maior numero é:",maior)
print(" o menor numero é:",menor)
        
#faca um programa que de uma ordem aleatoria de uma lista
import random

n1 = input("digite uma letra: ")
n2 = input("digite uma letra: ")
n3 = input("digite uma letra: ")
n4 = input("digite uma letra: ")

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(lista)
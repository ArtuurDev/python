#Faça um programa que leia 5 números e informe o maior número.

contador = 0
maior = 0
lista = []
while contador < 5:
    num = int(input("informe o numero:"))
    if num > 0:
        maior = num
        lista.append(num)
    contador = contador + 1
print(num)
print(lista)
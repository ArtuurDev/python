# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 



lista = []
for i in range(1,5):
    valor = int(input("digite um numero: "))
    lista.append(valor)
    print(lista)
print(f"o maior numero da lista é {max(lista)} e o menor é {min(lista)}")
print("o maior numero da lista está na posiçao {} e o menor está na posiçao {}".format(lista.index(max(lista)), lista.index(min(lista))))

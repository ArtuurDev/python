#Crie um programa onde o usuário possa digitar 
#cinco valores numéricos e cadastre-os em uma lista, já na 
#posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []

for i in range(5):
    v = int(input("digite um numero: "))
    if i == 0:
        lista.append(v)
    elif v >= lista[-1]:
        lista.append(v)
    elif v <= lista[0]:
        lista.insert(0,v)
print(lista)
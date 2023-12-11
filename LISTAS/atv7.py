#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
lista = []
peso = []
leve = []
while True:
    valores = [input("digite seu nome:"),int(input("digite seu peso:"))]
    lista.insert(0,valores)
    if lista[0][1] >= 70:
        peso.append(lista[0])
    else:
        leve.append(lista[0])
    end = input("quer sair? (S/N):").upper()
    if end == "S":
        print("o numero de cadastros foram {}".format(len(lista)))
        print("a lista das pessoas mais pesadas é {}".format(peso))
        print("a lista das pessoas mais leves é {}".format(leve))
        break


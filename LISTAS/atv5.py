#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_p= []
lista_i = []
while True:
    lista.append(int(input("digite um numero: ")))
    end = input("sair? (S/N)")
    if end == "s":
        break
for i in lista:
    if i % 2 == 0:
        lista_p.append(i)
    if i % 2 != 0:
        lista_i.append(i)
print("a lista com todos os numeros é",lista)
print("a lista com todos os numeros pares é",lista_p)
print("a lista com os numeros impares é",lista_i)
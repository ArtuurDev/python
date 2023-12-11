#Crie um programa onde o usuário possa digitar sete valores 
#numéricos e cadastre-os em uma lista única que mantenha 
#separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


lista = [[],[]]
for i in range(8):
    v = int(input("digite um valor: "))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)

lista[0].sort()
lista[1].sort()
print(f"todos os valores em uma unica lista é {lista}")
print("os valores pares em ordem crescente é {}".format(lista[0]))
print("os valores impares em ordem crescente é {}".format(lista[1]))

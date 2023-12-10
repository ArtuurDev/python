#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista= []
while True:
    n = int(input("digite um numero: "))
    lista.append(n)
    end = input("deseja encerrar o programa? (S/N)").upper()
    if end == "S":
        break
lista.sort(reverse=True)
print(f'na lista foram digitados {len(lista)} numeros')
print(" a lista na forma decrescente é {}".format(lista))
if 5 not in lista:
    print("o valor 5 nao esta na lista")
else:
    print("o numero 5 foi digitado")


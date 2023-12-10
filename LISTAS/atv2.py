#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []

while True:
    v =  int(input("digite um numero: "))
    if v in lista:
        print("valor duplicado nao vou adicionar")
    else:
        lista.append(v)
    
    end = input("quer encerrar o programa? (S/N):").upper()
    if end == "S":
        break

print(f"os valores contidos na lista sao {lista}")
print("e a lista em ordem crescente é:")
lista.sort()
print(lista)

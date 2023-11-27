

nome =(input("digite um nome: "))
print("o tipo primitivo dese nome é:", type(nome))
print(f' esse nome tem {len(nome)} caraqteres')


'''''
while True:
    saida = input("digite 'f' para sair: ").upper()
    if saida == "F":
        break

    num = int(input(" digite um numero:  "))
    num1 = int(input(" digite um numero: "))
    soma = num + num1
    print('O resultado da entre {} + {} é = {}'.format(num,num1,soma))
'''
lista = []
while True:
    saida = input("digite 's' para sair: ").upper()
    if saida == "S":
        break
    
    inteiros = int(input("digite os numeros para saber o quadrado: "))
    lista.append(inteiros)

lista  = [inteiros * inteiros for inteiros in lista] 
print(" O Quadrado dos numeros é:", lista)

#Faça um programa, utilizando for, que permita o
#usuário fazer três contas de subtração.
  
print("SUBTRAÇAO")
print("=" * 20)


for i in range(0,3):
    numero1 = int(input("digite um numero: "))
    numero2 = int(input("digite outro numero: "))
    sub = numero1 - numero2
    print(f'O resultado {numero1} - {numero2} é :{sub}')  
print("fim")  


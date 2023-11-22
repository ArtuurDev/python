

# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.





numero = int(input("digite um numero para saber se é primo ou nao: "))
intervalo = range(1,numero +1)
contador = 0
for num in intervalo:

    if numero % num == 0:
        print(f'o {numero} foi divisivel por {num}')
        contador +=1
if contador == 2:
    print(f'o numero {numero} é primo ')
elif contador > 3:
    print("composto")



#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.



tupla = (int(input("digite um numero: ")),(int(input("digite um numero: "))),(int(input("digite um numero: "))),(int(input("digite um numero: "))),)
print(tupla)

print(f'o valor 9 apareceu {tupla.count(9)} veses ')
if 3 in tupla:
    print(f'o valor 3 foi digitado na posiçao {tupla.index(3)}')
else:
    print("o valor 3, nao foi encontrado")
print("os numeros pares encontrados foram:")
for i in tupla:
    if i % 2 == 0:
        print(i,end=" ,")
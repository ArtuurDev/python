#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.


soma = 0
for i in range(1,7):
    n =  int(input("digite um numero par: "))
    if n % 2 == 0:
        soma += n
    if n % 2 != 0:
        print("O numero {} é nao é par".format(n))
print("o resultado da soma entre os 6 numeros é {}".format(soma))
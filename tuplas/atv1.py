#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


tupla = ("zero", "um", "dois", "tres", "quatro", "cinco")
tupla_ex = int(input("digite um numero de 0 a 5: "))

print("o numero digitado foi, {}".format(tupla[tupla_ex]))
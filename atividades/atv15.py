#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t = int(input("digite o primeiro termo: "))
r = int(input("digite a razão: "))
pa =  t
for i in range(1,10):
    pa += r 
    print("{}".format(pa),end="-")

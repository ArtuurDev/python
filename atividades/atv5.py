#faça um programa aque mostre a tabuada de um numero inteiro 


n = int(input("digite um numero: "))
for i in range(1,11): 
   print("{} * {} = {}".format(n, i,  n * i))




linguagens = ['java', 'javascript', 'c', 'c#']

novas_linguagens = [item.upper() for item in linguagens]

print(novas_linguagens)



numeros = [1,2,3,4,5,6,7,7,8,8,9,9,0]

#
numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_par)

numeros_par2 = []

#
for numero in numeros:
    if numero % 2 == 0:
        numeros_par2.append(numero)
        
print(numeros_par2)
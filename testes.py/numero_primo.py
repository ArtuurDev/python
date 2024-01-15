numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lista_primos = []
lista_nao_primos = []
for n in numeros:
    if n % 2 != 0:
        lista_primos.append(n)
    else:
        lista_nao_primos.append(n)

print('lista de numeros primos', lista_primos)
print('lista de numeros nao primos', lista_nao_primos)




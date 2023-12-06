#faça um programa que calcule  soma entre todos os numeros impares multiplos de 3 no intervalo de 1 a 500


soma = 0 

for i in range(0,501):
    if i % 3 == 0:
        soma = soma +i
        print(soma)
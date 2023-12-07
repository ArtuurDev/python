#faça um programa que calcule  soma entre todos os numeros impares multiplos de 3 no intervalo de 1 a 500


soma = 0 
imapares_divisivel3 = 0
for i in range(0,501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma +i
        imapares_divisivel3 +=1
print(" a soma entre os {} valores é {}".format(imapares_divisivel3,soma))
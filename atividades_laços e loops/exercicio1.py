#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário 
#informe um valor válido.

nota =  int(input("digite uma nota: "))


while nota < 0 or nota > 10:
    print(f'a nota {nota} é invalida')
    nota = int(input("digite uma nota: "))
    if nota < 0 or nota > 10:
        print(f'a nota {nota} é invalida')
    elif nota > 0 or nota < 10:
        print(f'a nota {nota} é valida') 
        break
print("fim")

#concluido
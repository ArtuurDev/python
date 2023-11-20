#faça um codigo que peça uma nota entre zero e dez. 
#mostre uma mensagem caso a nota seja invalida e 
#continue pedindo ate que o usuario informe uma nota valida

while True:
    nota = float(input("digite uma nota:"))
    if nota > 0 or nota < 10:
        print(f'a nota {nota} é invalida')
    if nota < 0 and nota > 10:
        print(f'a nota {nota} é valida')
        break    
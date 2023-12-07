#faça a tabuada de um numero que o usuario escolher 


while True:
    saida = input("para sair tecle 's':").lower()
    n = int(input("digite um numero: "))
    if saida == "s":
        break
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
#faça um programa com a funçao que necessite de um argumento. a funçao retorna "P",  se seu argumento for positivo, 
#e "N" se seu argumento por negativo



def sinal(numero):
    numero = "P" if numero > 0 else "N"
    return(numero)

numero = int(input("digite um numero: "))
numero = sinal(numero)
print(numero)
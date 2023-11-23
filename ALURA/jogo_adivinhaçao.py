#criando um jogo de adinvinhaçao
print("=" * 20)
print ("JOGO DE ADINVINHAÇAO!")
print("=" * 20)
print("CHUTE UM NUMERO DE 1 a 100")

tentativas = 5
import random
numero_secreto = (int(random.random() * 100)) # outa forma de fazer: random.randrage(1,100)
#print(numero_secreto) para ver o numero aleatorio
for rodada in range (1, tentativas + 1):
    print("tentativa", rodada, "de", tentativas)
    chute = int(input("chute um numero: "))
    if chute < 1:
        print("numero invalido")
        continue
    if chute == numero_secreto:
        print("VOÇE ACERTOU, PARABENS!!!!")
        break
    elif chute < numero_secreto:
        print("QUE PENA, VOÇE ERROU, TENTE UM NUMERO MAIOR!! ")
    elif chute > numero_secreto and chute < 101:
        print("QUE PENA, VOÇE ERROU, TENTE UM NUMERO MENOR!! ")
    else:
        if chute > 100:
            print("numero invalido")
print("o numero secreto é",numero_secreto)
print("fim do jogo")
    

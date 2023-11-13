#criando um jogo de adinvinhaçao
print("=" * 20)
print ("JOGO DE ADINVINHAÇAO!")
print("=" * 20)
print("CHUTE UM NUMERO DE 0 a 100")
print(input("PARA COMEÇAR PRESSIONE QUALQUER TECLA"))

tentativas = 3 
numero_secreto = 37

for rodada in range (1, tentativas + 1):
    print("tentativa", rodada, "de", tentativas)
    numero = int(input("chute um numero: "))
    if numero < 1:
        print("numero invalido")
        continue
    if numero == 37:
        print("VOÇE ACERTOU, PARABENS!!!!")
        break
    elif numero < 37:
        print("QUE PENA, VOÇE ERROU, TENTE UM NUMERO MAIOR!! ")
    elif numero > 37 and numero <= 100:
        print("QUE PENA, VOÇE ERROU, TENTE UM NUMERO MENOR!! ")
    else:
        if numero > 100:
            print("numero invalido")
    
    
print("fim do jogo")
    

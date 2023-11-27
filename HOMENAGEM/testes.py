print("=" * 20)

print("JOGUINHO DO AMOR ")
print("acerte todas as perguntas para ganhar um presente misterioso...")
print( "=" * 20)
tentativas = 0
começar = str(input("digite 'iniciar': "))

if começar == "iniciar" or começar == "Iniciar":
    dia_n = int(input("digite o dia que eu nasci: "))
if dia_n == 24:
    print("parabens mb, voçe acertou!!")
    print("vamos para proxima pergunta")
while dia_n != 24:
    print("vc perdeu, não vai ganhar o presente misterioso...")
    chance1 = input("para outra chance me de um beijo de lingua, aperte 'B':") 
    if chance1 == "b" or chance1 == "B":
            dia_n = int(input("digite o dia que eu nasci: "))
            if dia_n == 24:
                print("voçe acertou...")
                print("vamos para a proxima pergunta")
mes = input("digite o meu mes de nascimeto: ")
if mes == "fevereiro":
    print("voçe acertou!!")
while mes != "fevereiro":
    print("voçe errou...")
    mes = input("um beijo se quiser continuar..., digite 'b': ")
    if mes == "b" or mes == "B":
        mes = input("digite o meu mes de nascimeto: ")
        if mes == "fevereiro":
             print("voce acertou!")
print("vamos para proxima pergunta...")
nasci = int(input("em qual ano eu nasci?: "))
while nasci != 2006:
    nasci = str(input("voçe errou... um beijo para continuar, digite 'b': "))
    if nasci == "b" or nasci == "B":
        nasci = int(input("em qual ano eu nasci?: "))
if nasci == 2006:
    print("voçe acertou, amor!!")
    print("vamos para a proxima pergunta...")
print("foi facil até agora né? ")
print("vamos dificultar agora!")
s_idade = int(input("qual é a soma das nossas idades?: "))
while s_idade != 31:
    s_idade = (input("voçe errou, digite 'b' para continuar, mas antes vc me deve um beijo:  "))
    if s_idade == "b" or "B":
        s_idade = int(input("qual é a soma das nossas idades?: "))
if s_idade == 31:
    print("vc acertou, linda!")
print("proxima pergunta...")
conheceu = input("em que mes nos conhecemos?: ")
while conheceu != "outubro" and conheceu != "Outubro":
    conheceu = input("nao acredito vc errou, me beije para continuar: ")
    conheceu = input("digite 'b'")
    if conheceu == "b":
        conheceu = input("em que mes nos conhecemos?: ")
else:
    print("acertou!")



print("A proxima pergunta vc vai responder diretamente pra mim... ")

print(input("Quando foi a primeira vez que falei que te amava?"))
print("correto!!")
print(input("qual foi a primeira vez que disse eu te amo pra mim?"))
print("ai simm")
print(input("como foi nosso primeiro selinho?"))

print(input("no quarto da bea, como eu pedi pra vc deitar no meu ombro?"))

print(input("O que vc deseja pra nos no futuro?"))
print("É parece que vc vai ganhar seu presente")
print("e nao vai ser so um...")
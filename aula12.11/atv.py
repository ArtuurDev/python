
#Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem 
#COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.

#Obs.: você deve validar se a palavra tem três ou mais letras
#Obs.: você deve validar se a frase tem pelo menos 20 palavras
frase = input("digite uma frase:").split()
print()
print(frase)

while len(frase) < 2:
    frase = input("digite uma frase maior:")
palavra1 = input("digite uma palavra:")
print()
while len(palavra1) < 3:
    palavra1 = input("digite uma palvra maior ou igual 3 caracteres:")
print("VERIFICAÇAO DA PRIMEIRA PALAVRA DIGITADA")
print()
cont = 0
for i in frase:
    if i  == palavra1:
        print("A palavra '{}' aparece na frase, no indice {}".format(i,cont))
    cont +=1
print()
palavra2 = input("digite uma palavra:")
print()
print("VERIFICAÇAO DA SEGUNDA PALAVRA DIGITADA")
print()
while len(palavra2) < 3:
    palavra2 = input("digite uma palavra com 3 ou mais caracteres:") 
cont2 = 0
for i in frase:
    if i == palavra2:
        print("A palavra '{}' aparece na frase, no indice {}".format(i,cont2))
    cont2 +=1



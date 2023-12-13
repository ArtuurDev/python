#Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem 
#COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.

#Obs.: você deve validar se a palavra tem três ou mais letras
#Obs.: você deve validar se a frase tem pelo menos 20 palavras

frase = input("digite uma frase: ").lower().split("")

palavra = input("digite uma palvra:").lower()
while len(palavra) < 3:
    palavra = ("precisa ter mais de 3 caracteres:")

for i in frase:
    if i == palavra:
        print(i)
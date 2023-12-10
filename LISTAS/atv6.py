#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão 
#passada está com os parênteses abertos e 
#fechados na ordem correta

l = input("digite uma expressao:")
pilha = []
pilha2 = []
for i in l:
    if i == "(":
        pilha.append(i)
    if i == ")":
        pilha2.append(i)
if len(pilha) - len(pilha2) == 0:
        print("expressao valida")
else:
    print("expressao invalida")

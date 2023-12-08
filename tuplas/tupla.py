lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'pudim')
print(f"a bebida suco esta na posiçao {lanche.index('suco')}")
print(lanche.count('pudim'))

dados = ("artur", 17)
print(dados)
print(dados[0])
print(dados[1])



#tuplas sao imutaveis

#print(lanche[1])
#print(lanche[1][2])
#print(lanche[-2])
#print(sorted(lanche))
 
#tuplas sao imutaveis
#lanche[0] = 'trota'

for pos, i in enumerate(lanche):
    print(f"eu vomu comer {i} na posiçao {pos}")
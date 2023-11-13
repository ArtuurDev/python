# 1. crie uma lista com cinco nomes de alunos do curso de back-end
# a. imprima a lista
# b. adicione um sexto nome na lista
# c. remova o terceiro indice da lista 
# d. remova um objeto especifico na lista 
# e. imprima a lista 
# f. adicione um novo nome na lista 

lista = ['artur','mikael','elvis','cedex','jefersson']
print(lista)
lista.append('geisa')
del lista[2]
lista.remove('artur')
print(lista)
lista.append("alice")
print(lista)
# listas é representada pelos []
# len é um metodo que retorna a quantidade de itens de uma lista
# obs; todo metodo por obrigaçao ele retorna algum valor
lista = []
print(lista, type(lista))
print(len(lista))

lista = ['front']
print(lista, type(lista))
print(len(lista))

lista = ['back']
print(lista, type(lista))
print(len(lista))

lista.append('front')
print(lista, type(lista))
print(len(lista))

lista = ['back', 'tarde', 21, True, 8.8]
print(f' a quantidade de alunos na turma é: {lista[2]}')
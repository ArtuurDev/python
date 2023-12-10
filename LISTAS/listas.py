''''
lanche = ["açai"]
lanche.append("cookie")
print(lanche)
lanche.insert(1,"cachorro quente")
print(lanche)
del lanche[2]
lanche.pop(1)
lanche.remove("açai")
print(lanche)
print()

for i in range(3):
    v = int(input("digite um numero:"))
    lanche.append(v)
print(f"a lista final foi:{lanche}")
print("acabou")
'''
lista = [1,2,3,4,6,5,9,8,3,11,10]
lista.sort()
print(lista)

v = 15
lista.insert(-1,v)
print(lista)
''''
num = (2,8,4,5,6,)
lista = list(num)
print(lista)
lista[0] = 10
print(lista)

lista.append(11)
print(lista)
lista.sort()1
print(lista)
lista.sort(reverse=True)
print(lista)
print(len(lista))
print()
print()


for i in lista:
    if i % 2 != 0:
        lista.remove(i)
        print(lista) 
'''
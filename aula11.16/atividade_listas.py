# imprima na tela os pares dentro de uma lista chamada pares_ok
# remova da lista os multiplos de 4

meus_numeros = [0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares_ok = []
pares_ok = meus_numeros[0::2]
print(pares_ok)
pares_ok.remove(0)
pares_ok.remove(4)
pares_ok.remove(8)
pares_ok.remove(12)
pares_ok.remove(16)
pares_ok.remove(20)
print(pares_ok)
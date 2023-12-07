#faça um codigo que peça a marca e o modelo do carro do cliente e insere ele em ula liata e deoois traform em um dicionario. imprima os dois resultados


lista =[]
marc = (input("qual a marca do seu carro: "))
modelo = (input("digite o modelo do seu carro: "))


lista.append(marc)
lista.append(modelo)
print(lista)

dic = {}

dic.update([lista])
print(dic)
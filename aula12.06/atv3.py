#faça um codigo que peça a marca e o modelo do carro do cliente e insere ele em ula liata e deoois traform em um dicionario. imprima os dois resultados


modelo = input('digite a marca do seu carro: ')
marca = input('digite a modelo do seu carro: ')

lista = [modelo, marca]

dic = {}
dic.update([lista])


print(dic)
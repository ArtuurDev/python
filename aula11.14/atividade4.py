#faça um código que pede 5 letras e quando for consoante ele avisa "É uma consoante", imprima uma lista com as consolantes encontradas



letra1 = (input("digite primeira letra:"))
letra2 = (input("digite segunda letra:"))
letra3 = (input("digite terceira letra:"))
letra4 = (input("digite quarta letra:"))
letra5 = (input("digite quinta letra:"))
lista_consoantes = []
if letra1 != "a" and letra1 != "A" and letra1!= "a" and letra1 != "e" and letra1 != "E" and letra1 != "i" and letra1 != "I" and letra1 != "o" and letra1 != "O" and letra1 != "u" and letra1 != "U":
    print("a letra um é consoante")
    lista_consoantes.append(letra1)
elif letra1 == "a" or letra1 == "A" or letra1 == "a" or letra1 == "e" or letra1 == "E" or letra1 == "i" or letra1 == "I" or letra1 == "o" or letra1 == "O" or letra1 == "u" or letra1 == "U":
    print("A letra um é uma vogal")
if letra2 !=  "a" and letra2 != "A" and letra2 != "a" and letra2 != "e" and letra2 != "E" and letra2 != "i" and letra2 != "I" and letra2 != "o" and letra2 != "O" and letra2 != "u" and letra3 != "U":
    print("a letra dois é uma consoante")
    lista_consoantes.append(letra2)
elif letra2 == "a" or letra2 == "A" or letra2 == "a" or letra2 == "e" or letra2 == "E" or letra2 == "i" or letra2 == "I" or letra2 == "o" or letra2 == "O" or letra2 == "u" or letra2 == "U":
    print("A letra dois é uma vogal")
if letra3 !=  "a" and letra3 != "A" and letra3 != "a" and letra3 != "e" and letra3 != "E" and letra3 != "i" and letra3 != "I" and letra3 != "o" and letra3 != "O" and letra3 != "u" and letra3 != "U":
    print("a letra três é uma consoante")
    lista_consoantes.append(letra3)
elif letra3 == "a" or letra3 == "A" or letra3 == "a" or letra3 == "e" or letra3 == "E" or letra3 == "i" or letra3 == "I" or letra3 == "o" or letra3 == "O" or letra3 == "u" or letra3 == "U":
    print("A letra tres é uma vogal")
if letra4 !=  "a" and letra4 != "A" and letra4 != "a" and letra4 != "e" and letra4 != "E" and letra4 != "i" and letra4 != "I" and letra4 != "o" and letra4 != "O" and letra4 != "u" and letra4 != "U":
    print("a letra quatro é uma consoante")
    lista_consoantes.append(letra4)
elif letra4 == "a" or letra4 == "A" or letra4 == "a" or letra4 == "e" or letra4 == "E" or letra4 == "i" or letra4 == "I" or letra4 == "o" or letra4 == "O" or letra4 == "u" or letra4 == "U":
    print("A letra quatro é uma vogal")
if letra5 != "a" and letra5 != "A" and letra5 != "a" and letra5 != "e" and letra5 != "E" and letra5 != "i" and letra5 != "I" and letra5 != "o" and letra5 != "O" and letra5 != "u" and letra5 != "U":
    print("a letra cinco é uma consoante")
    lista_consoantes.append(letra5)
elif letra5 == "a" or letra5 == "A" or letra5 == "a" or letra5 == "e" or letra5 == "E" or letra5 == "i" or letra5 == "I" or letra5 == "o" or letra5 == "O" or letra5 == "u" or letra5 == "U":
    print("A letra cinco é uma vogal")

print(lista_consoantes)


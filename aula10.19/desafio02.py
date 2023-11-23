#Receba a altura de uma pessoa, crie um codigo que calcule o peso ideal.
while True:
    end = input("digite 'e' para encerrar")
    if end == "e" or end == "E":
        break
    sexo = input("informe seu sexo: feminino(f) mascuino(m):")
    if sexo == "m" or sexo == "M":
        masculino_h = float(input("digite sua altura:"))
        peso_ideal = float(72.7 * masculino_h) - 58
        print("seu peso ideal é:", peso_ideal)
    else:
        feminino = input("digite sua altura:")
    
while True:
    nota = int(input("informe a nota:"))
    if nota <  0 or nota > 10:
        break
print(f'nota {nota}, é maior que 10')

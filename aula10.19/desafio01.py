#crie um código que peça a temperatura em graus Fahrenheit, trasforme e imprima a temperatura em graus celsius. 

temperatura_F = float(input("digite a temperatura em fahrenheit:"))
temperatura_C = float(5) * ((temperatura_F - 32) / 9)

print("A temperatura em fahrenheit é:", temperatura_F)
print("temperatura fahrenheit convertida em celsius é:", temperatura_C)
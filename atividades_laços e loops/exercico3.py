#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("qual é o seu nome? (minimo 4 caracteres).: ")
while len(nome) <=3:
    nome = input("seu nome deve ter no minimo 4 caracteres:")

idade = (int(input("digite sua idade entre 0 e 150 anos: ")))
while idade < 0 or idade > 150:
    idade = input("erro.Voçe deve ter entre 0 e 150 anos:")

salario = int(input("qual é o seu salario?  "))
while salario < 0:
    salario = int(input("nao existe salario negativo. tente novamente..."))  

sexo = input("informe seu sexo, 'f' para feminino 'm' para masculino: ")
while sexo != "f" and sexo != "m":
    sexo = input("informe seu sexo, 'f' para feminino 'm' para masculino:")

civil = input("qual seu estado civil? (s) para solteiro, (c) para casado, (v)para viuvo/a")
while civil != "s" and civil != "c" and civil != "v":
    civil = input("qual seu estado civil? (s)para solteiro, (c)para casado, (v), para viuvo/a:")
    
print("cadastro concluido")


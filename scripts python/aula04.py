# solicite um número e exiba uma tabuada desse número de 1 a 10

'''import time

numero = int(input("digite um número para tabuada  "))

for contador in range(1,11):
    multiplicar = numero*contador
    time.sleep(0.5)
    print(f"{numero}x{contador} = {multiplicar}")'''


#soma de número de 1 a 100
'''soma = sum(range(1,101))
print(f" a soma dos números de 1 a 100 é: {soma}")'''
#programa que solicita ao usuário um nome e depois exibe cada caractere
'''palavra = input("digite uma palavra  ")

for letra in palavra:
    print(letra)'''

#contagem regreciva de 10 a 1 e feliz ano novo no final
'''import time
for numero in range(10,0,-1):
    time.sleep(0.5)
    print(numero)
time.sleep(0.5)
print("feliz ano novooo!!!!")'''

#programa que solicita 10 números ao usuário e depois exibe os números digitados, os pares e os impares
'''numeros = []
par = []
impar = []

for contador in range(10):
    numero = int(input(f"digite o {contador+1} número"))
    numeros.append(numero)

for numero in numeros:
    if numero %2 == 0:
       par.append(numero)
    else:
        impar.append(numero)
print(f"os números digitado são:{numeros}")
print(f"os números pares são:{par}")
print(f"os números impares são:{impar}")'''

#soma de números pares

'''soma = sum(range(2,52,2))
print(f" a soma dos números pares de 1 a 50 é  {soma}")'''

#contagem de vogais em uma palavra

'''palavra = input("digite uma palavra  ")
vogais = ["a","e","i","o","u"]
contador = 0

for letra in palavra:
   if letra.lower() in vogais:
    contador += 1
print(contador)'''


notas = []

for contador in range(5):
    nota = float(input(f"digite sua {contador + 1} nota "))
    notas.append(nota)
    media = notas + contador /5
    

print(media)
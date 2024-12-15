numero1 = int(input("digite o primeiro número  "))
numero2 = int(input("digite o segundo número  "))

if numero1 >= numero2:
     print("o 1 número digitado tem que ser menor que o 2 número digitado")

else:
 if numero1 %2 != 0:
    numero1 += 1
 soma = 0
 for numero in range(numero1,numero2+1,2):
    
    print(numero)
    soma += numero
print(f" a soma dos números pares de {numero1} até {numero2} é {soma}")
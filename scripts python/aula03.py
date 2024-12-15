#contagem de números de 1 à 10
'''import time
inicial = int(input(" digite o número inicial  "))
final = int(input(" digite o número final  "))
contador = inicial
while contador <= final:
    print (f"seu núemro atual é  {contador}")
    time.sleep(0.3)
    contador +=1'''

#somar todos os números de 1 à 100


'''inicio = int(input(" digite o número inicial  "))
fim = int(input("digite o número final  "))
if (inicio > fim):
    print ("erro de digitação, o número inicial deve ser menor que o final")
else:
    soma_total = 0
    numero_atual = inicio
    while numero_atual <= fim:
        soma_total+= numero_atual
        numero_atual += 1
    print(f" a soma dos nùmeros de {inicio} até {fim} é {soma_total}")'''

    # solicite ao usuário que digite um número depois faça a tabuada desse número através de um while

'''import time
numero = int(input("digite um número de 1 à 10  "))
contador = 1

while contador <=10:
    resultado = numero * contador
    print(f"{numero} * {contador} = {resultado}")
    time.sleep(0.5)
    contador += 1'''

# contagem regressiva para o ano novo usando while

'''import time
inicio = 10
fim = 1
contador = inicio
while contador >= fim:
    print(contador)
    time.sleep(0.5)
    contador -= 1
  
print("feliz ano novo!!!!!!")'''

# solicite ao usuário para digitar um número e o programa vai fazer a contagem de 1 até o número digitado mas mostrando só os impares
'''import time
numero = int(input(" digite um número  "))
contador = 1
while contador<=numero:
    
    print(contador)
    time.sleep(0.5)
    contador +=2'''
# solicitar um número ao usuário até que ele digite um número negativo somando apenas os números positivos

'''numeros_positivos = []

while True:
    numero = int(input(" digite um número positivo ou negativo  "))
    if (numero <0):

        break
    numeros_positivos.append(numero)
soma = sum(numeros_positivos)
print(f" a soma dos números positivos digitados são:{soma}")'''

# programa que solicita um número ao usuário para fazer a tabuada desse número mas só exibe os números que forem multiplos de 3
'''import time
numero = int(input(" digite um número de 1 à 10  "))
contador = 3
if (numero >10 or numero < 0):
    print("favor digitar um número de 1 à 10")
else:
    while contador <=10:
        resultado = contador * numero
        print(f"{numero} * {contador} = {resultado}")
        time.sleep(0.5)
        contador += 3'''
# programa em que o usuário digita as notas até digitar -1, depois calcula e exibe a média das notas

'''media_nota = []

while True:
    nota = float(input("digite sua nota ou digita -1 para sair  "))
    if nota == -1:
     break
    elif 0<= nota <=10:
        media_nota.append(nota)
    else:
        print("número digitado invalido favor digitar um número de 1 à 10")

if len(media_nota):
    soma = sum(media_nota)
    media = soma / len (media_nota)
    print(f" as notas digitadas foram:{media_nota}")
    print(f" a soma dos núemros digitados é:{soma}")
    print(f" a media das notas é:{media}")'''
# criar uma contagem de 1 à 10 com while que termine quando chegar no 10

'''import time
inicio = 1
fim = 11
contador = inicio

while True:
    if contador == fim:
     break
    else:
        print(contador)
        time.sleep(0.5)
        contador+= 1'''
# criar um programa de some os números de 1 à 50 parando no número 50

'''inicio = 1
fim = 51
numero_atual = inicio
soma_total = 0

while True:
 if numero_atual == fim:
    break
 else:
  soma_total+=numero_atual


  numero_atual+=1
print(f" a soma dos números de 1 à 50 é:{soma_total}")'''
#Crie um programa que solicite ao usuário um número entre 1 e 10 Continue pedindo até que o usuário forneça um valor válido.

'''numero_correto = 5
while True:
    numero = int(input(" digite um número de 1 à 10 "))
    if numero == numero_correto:
        print("número válido")
        break
    else:
        print("número incorreto")'''
#Desenvolva um programa que peça ao usuário para digitar uma
#senha e continue pedindo até que a senha correta (previamente
#definida) seja inserida.

'''senha_correta = 12345

while True:
    senha = int(input(" digite a senha de 5 digitos "))
    if senha == senha_correta:
        print("acesso liberado")
        break
    else:
        print("senha incorreta")'''

    

















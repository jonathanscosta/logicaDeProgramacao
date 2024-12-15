
#identifique se o número é positivo negativo ou zero

numero = float(input(' digite um número   '))

if(numero > 0):
    print(f'o número {numero:.0f} é positivo')
elif (numero < 0 ):
    print (f' o número {numero:.0f} é negativo')
else:
    print (f' o número {numero:.0f} é zero')


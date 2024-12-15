

#verificar se as idades são maiores, menores ou iguais

'''usuario1 = int(input('qual sua idade?   '))
usuario2 = int(input('qual sua segunda idade?   '))

if ( usuario1 > usuario2):
    print ('a idade do usuario 1 é maior que usuario2')
elif ( usuario2 > usuario1):
    print ('a idade do usuario 2 é maior que usuario1')

else:
    print ('as idades são iguais')'''

# verificar se os nomes são iguais ou diferentes

'''nome1 = input (' qual seu nome?  ').lower() .strip()

nome2 = input (' qual seu nome?  ').lower() .strip()

if (nome1 == nome2):
    print ('seus nomes são iguais')
else:
    print (' seus nomes são diferentes')'''

# verificar se o individuo pode dirigir ou não
'''idade = int (input('qual sua idade?  '))
habilitacao = input(' você possui habilitação (sim ou não)')

if (idade >= 18 and habilitacao == 'sim' ):
    print ( ' você pode dirigir')
else:
    print (' você não pode dirigir')'''

# verifica se o aluno passou ou não na média

'''bimestre1 = int (input(' qual sua nota no primeiro trimestre? '))
bimestre2 = int (input(' qual sua nota no segundo trimestre? '))
bimestre3 = int (input(' qual sua nota no terceiro trimestre? '))
bimestre4 = int (input(' qual sua nota no quarto trimestre? '))

nota = (bimestre1 + bimestre2 + bimestre3 + bimestre4) /4

if ( nota >= 6 ):
    print (f' aluno aprovado, sua nota foi {nota}')
else:
    print (f'aluno reprovado, sua nota foi {nota}')'''

# desconto de 5% no produto

'''produto = 100
desconto = 5/100

produto -= produto * desconto

print (f'seu desconto foi {produto:.2f}')'''

# dobro do valor de um produto

'''produtoBlackfraude = 100
produtoBlackfraude *= 2

print(f' produto está com desconto de: {produtoBlackfraude:.2f}')'''

# verificar se o caractere está na frase ou não

'''frase = input ('digite uma frase')
caractere = input (' digite uma palavra')

if ( caractere in frase):

    print(f' o caracter {caractere} está na frase')

else:
    print(f' o caracter {caractere}  não está na frase')'''

# verificar se uma palavra está em uma frase

'''frase = input ('digite uma frase')
palavra = input (' digite uma palavra')

if ( palavra in frase):

    print(f' a palavra {palavra} está na frase')

else:
    print(f' a palavra {palavra} não está na frase')'''

#ver se um número é par ou impar

'''usuario = int(input('digite um número:  '))
if (usuario %2==0):
    print (' seu número é par')
else:
    print (' seu número é impar')'''

# verificar aprovação de um aluno com nota maior que 6
'''nota1trimestre = int(input('qual sua primeira nota?'))
nota2trimestre = int(input('qual sua segunda nota?'))
nota3trimestre = int(input('qual sua terceira nota?'))
nota4trimestre = int(input('qual sua quarta nota?'))

notaFinal = (nota1trimestre + nota2trimestre + nota3trimestre + nota4trimestre)/4

if (notaFinal >=6):
    print ('aluno passou')
else:
    print ('aluno não passou')'''

#ver se o número é par ou impar e se é negativo ou positivo

'''numero = float (input ('digite seu número'))

if ( numero > 0):
    sinal = "positivo"
elif (numero <0):
    sinal = 'negativo'
else:
    sinal = 'zero'
if (numero %2 == 0):
    par_impar = 'par'
else:
    par_impar = 'impar

    
    
print (f'o número {numero} é {par_impar} e {sinal}')'''

#calcular o imc ( p.s esse deu trabalho kkk)

'''peso = float (input ('digite seu peso   '))
altura = float (input(' digite sua altura  '))

imc = peso / (altura ** 2)

print (f'o seu imc é {imc:.2f}')

if (imc < 18.5):
    print (' você está abaixo do peso')
elif (18.5 <= imc < 24.9):
    print (' você tem um peso normal')
elif (24.9 <= imc < 29.9):
    print (' você está acima do peso')
elif ( 30 <= imc <34.9):
    print (' você é obeso')
else:
    print (' vai já papocar com linha e tudo')'''

# login simples login: admin e senha: 1234



'''login = input(' login   ')
senha = input(' senha   ')

if ( login == 'admin' and senha == '1234'):
    print(' acesso liberado')
else:
    print (' acesso negado')'''

# verificar se um desconto pode ser aplicado somente a partir de 10 unidades

valorProduto = float (input (' qual o valor do produto?    '))
quantidadeProduto = float (input (' quantas unidades do produto?    '))
desconto = 10/100


if (quantidadeProduto >=10):

    valorProduto -= valorProduto * desconto
    print(f'o valor do produto é {valorProduto:.2f}')


else:
   print(f'o valor do produto é {valorProduto:.2f}')

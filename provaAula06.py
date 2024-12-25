login = input("digite seu login  ").lower().strip()
senha = int(input("digite sua senha de 5 digitos  "))
loginCorreto = 'jonathan'
senhaCorreta = 12345
tentativas = 3

while tentativas >0:
    if login == loginCorreto and senha == senhaCorreta:
        print("acesso liberado")
        break
    else:
        tentativas -=1
        if tentativas>0:
            print(F"seu login ou senha estão errados você tem {tentativas} tentativas")
            login = input("digite seu login novamente  ").lower().strip()
            senha = int(input("digite sua senha novamente  "))
else:
    print("suas tentativas acabaram")
if tentativas == 0:
    for errar in range(3)
    print ("acesso negado")


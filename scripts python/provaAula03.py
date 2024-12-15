#jogo de adivinhação usando laço while

numero_certo = 7
tentativa = 3

print("bem vindo ao jogo de adivinhação digite um número de 1 a 10")
print(f" você tem {tentativa} tentativas")

while tentativa > 0:
    palpite = int(input("digite seu palpite  "))

    if palpite == numero_certo:
        print(f"parebens o número certo é {numero_certo}")
        break
    else:
        tentativa -= 1
        if tentativa > 0:
         print(f"numero errado você tem mais {tentativa} tentativas")

        else:
           print(f" que pena suas tentaivas acabaram o número correto era {numero_certo}")

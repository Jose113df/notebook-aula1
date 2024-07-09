import random

numeroSecreto =random.randint(1,20)

tentativas = 0
maxTentativas = 5
acertou = False
print("Bem vindo ao game")
print(f"Numero maximo de tentativas = {maxTentativas}")

#loop

while tentativas < maxTentativas:
    palpite = int(input("Digite um numero inteiro: "))
    
    tentativas += 1

    if palpite == numeroSecreto:
        acertou = True
        break

    elif palpite < numeroSecreto:
        print("Tente um numero MAIOR")
        
    else:
        print("Tente um numero MENOR")

if acertou:
        print(f"Você acertou!!! Parabens, o numero era {numeroSecreto}")

else:
        print("Que pena você não conseguiu adivinhar o nuemro secreto")
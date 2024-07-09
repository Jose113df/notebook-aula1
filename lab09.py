import random
listaNome=[]
while True:
    nome=input("Digite os nomes que serão sorteados: ")
    if nome != "":
        listaNome.append(nome)
    else:
        break

escolhido = random.choice(listaNome)

print(escolhido)

print()
print(listaNome)


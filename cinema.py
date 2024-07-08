import os
import time

os.system("cls")
nome= input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while True:
    if nome != "":
        print("SALA 1: John Wick 3 (+16)")
        print("SALA 2: Divertidamente 2 (L)")
        print("SALA 3: Um lugar silencioso Dia 1 (+18)")
        print("SALA 4: Miranha Myles Morales 2 (12)")
        print("SALA 5: Show Cold Play Music of the Spheres (L)")
        sala = int(input("Digite a sala que deseja assistir: "))
        

        if sala == 3 and idade >= 18:
            print("CINEMARK")
            print(30*"-","INGRESSO",30*"-")
            print("FILME: Um lugar silencioso Dia 1 (+18) ")
            print("SALA: ",sala)
            print("NOME: ",nome)
            print("ASSENTO: A SUA ESCOLHA")
            print(78*"-")
            break
        elif sala == 1 and idade >= 16:
            print("CINEMARK")
            print(30*"-","INGRESSO",30*"-")
            print("FILME: John Wick 3 (+16) ")
            print("SALA: ",sala)
            print("NOME: ",nome)
            print("ASSENTO: A SUA ESCOLHA")
            print(78*"-")
            break
        elif sala == 4 and idade >= 12:
            print("CINEMARK")
            print(30*"-","INGRESSO",30*"-")
            print("FILME:  Miranha Myles Morales 2 (+12) ")
            print("SALA: ",sala)
            print("NOME: ",nome)
            print("ASSENTO: A SUA ESCOLHA")
            print(78*"-")
            break 
        elif sala == 2 and idade > 0:
            print("CINEMARK")
            print(30*"-","INGRESSO",30*"-")
            print("FILME:  Divertidamente 2 (L) ")
            print("SALA: ",sala)
            print("NOME: ",nome)
            print("ASSENTO: A SUA ESCOLHA")
            print(78*"-")
            break 
        elif sala == 5 and idade > 0:
            print("CINEMARK")
            print(30*"-","INGRESSO",30*"-")
            print("FILME: Show Cold Play Music of the Spheres (L) ")
            print("SALA: ",sala)
            print("NOME: ",nome)
            print("ASSENTO: A SUA ESCOLHA")
            print(78*"-")
            break 
        else:
            os.system("cls")
            print("Sua idade não permite ver esse filme ")
            print("Escolha outro filme")
            time.sleep(3)
        continue
    else:
        os.system("cls")
        print("Até mais ")
        time.sleep(3)
        break
        
    
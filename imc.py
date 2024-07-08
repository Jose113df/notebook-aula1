import os 
import time
while True:
        nome = input("Digite seu nome (aperte enter para sair)")

        if nome != '':
                peso = input("Digite seu PESO para o Calculo do IMC: (peso em KG)").replace(",",".")
                altura = input("Digite a sua altura SEM A VIRGULA (Altura em cm): ").replace(",",".")
                peso = float (peso)
                altura = float (altura)
                imc =   (peso / (altura * altura))
                if imc > 40:
                        print("Você está com grau de obesidade II. IMC: ", imc) 
                elif imc > 35:
                        print("Você está com grau de obesidade I. IMC: ",imc) 
                elif imc > 30:
                        print("Você está acima do peso. IMC: ",imc) 
                elif imc > 25:
                        print("Você está no peso ideal. IMC: ",imc) 
                elif imc > 18.5:
                        print("Você está abaixo do peso. IMC: ",imc) 
                elif imc > 17:
                        print("Você está com anorexia. IMC: ",imc) 
                else:
                        print("Você está com grau de obesidade mórbida. IMC: ",imc)
                continue
                
                
    
        else:
                break


'''
comentario em bloco 

'''

#comentario em linha 

'''
nome = "gomes"

print(nome)

peso = 80.5
altura=1.74
instrutor = True 
print(peso)
print(altura)
print(instrutor)
print(type(instrutor))
print(type(peso))
print(instrutor, type(instrutor))


valor = 15
print(valor, type(valor))
valor = str(valor)
print(valor, type(valor))
'''
'''
nome = input("Digite seu nome ")
idade = int(input("Digite a sua idade "))

if idade>17:
    print(nome," é maior de idade, IDADE: ",idade)
else:
    print (nome," NÃO é maior que 18 anos, IDADE: ",idade )


#tipos de concatenação
print("olá meu nome é ",nome, "tenho ",idade," anos.")

print("olá meu nome é "+nome+ "tenho "+str(idade)+" anos.") #Concatenação só vai com tipo STRING precisa converter os dados 

print(f"olá meu nome é {nome}, tenho {idade} anos.")
'''
'''
nome = input("Digite seu nome ")
idade = int(input("Digite a sua idade "))
peso = float(input("Digite a seu peso "))
altura = float(input("Digite a sua altura "))

#primeiro tipo de concatenação
print(f"Olá meu nome é {nome}, tenho {idade} anos, meu peso é {peso} e tenho {altura} de altura")
#segundo tipo de concatenação
print("Olá meu nome é ",nome,", tenho ",idade," anos, meu peso é ",peso," e tenho ",altura," de altura") 
#terceiro tipo de concatenação
print("Olá meu nome é ",str(nome),", tenho ",str(idade)," anos, meu peso é ",str(peso)," e tenho ",str(altura)," de altura") #terceiro tipo de concatenação
'''

#Declaração de variavel
nome="jose"

#Converter tipo de variavel
valor=15
valor = str(valor)

# restringir os dados 
idade = int(input("Digite a sua idade "))


#Git 


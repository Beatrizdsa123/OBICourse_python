#tupla nao consegue alterar, usa parenteses
dados = [("Ana", 8), ("Carlos, 6")]

print(dados)

nome = (input("nome"))
nota = (int(input("nota")))

dados.append((nome,nota))

print(dados)

#simulacao 
#lacos de repeticao for i in range e while e if o count (count += 1)


#FLUXO
#inicializar variaveis repetir

numeros  = [2,3,4,5,6,7]

pares = 0

for x in numeros:
    
    if x % 2 == 0:
        pares += 1
        
print("quantidade de pares: ", pares)


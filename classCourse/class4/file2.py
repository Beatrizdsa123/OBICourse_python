dados = []
'''
while True:
    nome = (input("nome: "))
    nota = (float(input("nota: ")))
    dados.append((nome, nota))
    
    x = input("Deseja continuar? s para sim ")
    
    if x != 's':
        break
print(dados)


for nome, nota in dados:
    if nota >=7:
        print(nome)
        

#errado
h = int(input("altura: "))
qtd = int(input("quantidade de casas"))

j=0
while h>=0:
    h -= qtd
    j += 1

    print("o tanto de jogadas ", j)
'''
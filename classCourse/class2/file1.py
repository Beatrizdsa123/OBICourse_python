# listas e tuplas
'''armazena valores, mutaveis, acessados por indice'''
# strng, texto, numero, vazia
valores = [10, 6, 124]
mista = [1, 'texto',  14, True]  # pode misturar
vazia = []

# Percorrendo a lista com um loop for
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

lista = [1,2,3,4,5,2,2,2,2]

#METODOS: ---------------------------------------------------------------------------------------------------------------
#len(le quantos elementos tem na lista, len(lista));
len(lista)

#append(adiciona no fim da lista, lista.append(5));
lista.append(6)

#insert(inserir escolhensdo  posiçao com dois parametros, lista.insert(5,10));
lista.insert(10,2)

#pop (trabalha com indice, remove o ultimo elemento mas pode colocar a posicao, lista.pop(0) passa a posicao);
lista.pop() 
lista.pop(2)

#remove trabalha com o valor literalmente
lista.remove(3)

#para remover todos "2" da lista
valor = 2
while valor in lista:
    lista.remove(valor)
    
#sort: ordena a lista
lista.sort()#agora a lista tem o novo valor ordenado
lista2 = ['wagner', 'ana', 'larissa']

print(lista2.sort())

#sorted ordena mas nao altera a lista, alera naquele momento que e usada mas nao substitui o valor original
sorted(lista) #altera so nessa linha
lista3 = ['976236', '20534', '11234']
print(sorted(lista3))

#min/max
min(lista)
max(lista)

#sum soma dos elementos da lista
sum(lista)

#metodo
#copiar listas

nova = lista[:]
novalista = list(lista)

lista5 = [2,3,4]
#split    separa entrada separa por espacao 
lista4 = input().split() #pode tbm por ; split(';')

print(lista4)
#map 
#converte para inteiro todas as separadas pelo split um coloca aspas e o split tira as as aspas que o split colocou 
#split string com aspas , map numero sem aspas
lista = list(map(int, input().split()))

list(map(int, input().split))    #separa a entrada por padrao em espacos 
                                                                                                                                                                                                                                                                                                                     
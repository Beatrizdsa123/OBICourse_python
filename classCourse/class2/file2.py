lista = [2,2,2,2,2,3,4,5]
print(len(lista))

while (len(lista) > 5):
    print(lista.pop())
    
#atividade
lista2 = []

ask = input("voce quer adicionar valor? (sim/ não)").lower().strip()

if ask == 'sim':
    
    
    while  ask == 'sim':
        
        num = input("Qual valor? ")
        lista2.append(num)
        print(lista2)
        ask = input("voce quer adicionar valor? (sim/ nao)").lower().strip()
        if ask == "não":
            print("saiu do programa")

else:
    print("saiu do programa")
    
#atividade 2

lista = []

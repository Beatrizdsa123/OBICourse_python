#upper(), lower(), in s()

texto ="OLá mundo"


#1 concatenar strings:
print("1. concatenar strings:")
print("Hello" + " " + "World" )

#2 repetir uma string

print("\n2. Repetir uma string: ")
print("ha" * 3)

#3 

#4 fatiar
print("\n4. fatiar(slicing): ")
print(texto[2:7])

#5 tamanho da string conta quantos caracteres tem
print("\n5. Tamanho da string: ")
print(len(texto))

#6 converter para maiusculas
print(texto.upper())

#7 converter para  maiusculas
print(texto.lower())

#8 deixa so a 1 maiuscula
print(texto.capitalize())

#9 inicial maiuscula para cada palavra
print(texto.title())

#10 remover espacos do inicio ao fim 
print(texto.strip())

#11 substituir parte da string
print(texto.replace("incrível", "poderoso"))

#12 verificar se contem 'python"
print("Python" in texto) 

#13 contar quantas vezes algo aparece
print(texto.count("!"))

#14
#15
#16
#17
#18
#19
#20 juntar lista de strings
string = texto.split(" ")
print("".join(string))

letra = input("Digite uma letra: ")
frase = input("Digite uma frase: " )

if len(letra ) == 1:
    quantidade = frase.count(letra)
    print(f"Aletra '{letra} aparece {quantidade} de vezes")
    
else:
    print("digite uma resposta valida")
    
    

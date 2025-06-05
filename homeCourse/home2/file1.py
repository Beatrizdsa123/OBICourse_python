#aula 24/05 - if, for e while

#IF- e uma bifurcacao onde ha escolhas 
#exemplo1
tempo = int(input("Quantos anos o eu carro tem? "))

if tempo <= 3:
    print("seu carro é novo")
elif tempo > 3:
    print("Seu carro é velho")
else:
    print("Digite um valor válido")

#exemplo2
nome = str(input("Qual é o seu nome? "))

if nome == "Beatriz":
    print("Que nome lindo você tem")
print(f'Bom dia, {nome}')

#exemplo3
n1 = float(input("Qual a sua nta 1? "))
n2 = float(input("qual a sua nota 2"))

media = (n1 + n2)/2

print(f"Sua média foi {media}")

if media >= 6:
    print("Sua média foi boa, parabéns")
else:
    print("Sua média foi ruim, estude mais")

#FOR
#exemplo1
for c in range(0,6):
    print('oi')
print('fim')

#exemplo2
n = int(input('Digite um número'))

for c in range(0, n+1): # 0 inicio,  n+1 fim
    print(c)
print('fim')

#exemplo3
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range(i, f+1, p): #i - inicio, f+1 - fim, p - iterador 
    print(c)
print('fim')

#exemplo4
frase = 'Ola mundo'

for caracter in frase:
    print(caracter)

#exemplo5
numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)

#WHILE
#exemplo1
c = 1 #contador
while c <= 10:
    print(c)
    c += 1 #IMPORTANTE iterar o contador

#usado quando eu n sei ate que numero exato vai

#exemplo2
r = 'S'
while r == 'S':
    n = int(input("Digite um valor: "))
    r = input("Quer continuar: ").upper()

print("fim")


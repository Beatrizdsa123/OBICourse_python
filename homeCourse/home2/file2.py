#desafio1 - if
from random import randint
computador = randint(0,5)
print("pensando" '-=-' * 20)
usuario= int(input("Qual o numero o computador pensou: "))

if computador == usuario:
    print("Usuário voce acertou")

elif computador != usuario:
    print("Usuario você errou")

else:
    print("Digite um valor válido")

#desafio2 - if

vel = int(input("Qual a velocidade do carro em Km/h: "))

if vel >= 80:
    print("Seu carro foi multado")
    multa = (vel-80) *7
    print(f"A multa foi de {multa} R$")
else:
    print("Prabéns você não foi multado")

#desafio3 - if

num = int(input("Qual o numero? "))

if num %2 == 0:
    print("É um número par")

else:
    print("É um número impar")

#desafio 4 - 

for i in range(2,50+2,2):
    print(i)
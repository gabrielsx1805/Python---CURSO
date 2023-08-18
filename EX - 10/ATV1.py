import random

x = random.randrange(0,6)
num = int(input("Digite um numero: "))

if  num == x:
    print("Voce acertou!")
else:
    print("Voce errou!")
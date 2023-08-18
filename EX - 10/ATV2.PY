vel = float(input("Digite a velocidade: "))

if vel > 80.0:
    print("Você foi multado!")
    print("Valor da multa é R$ {}".format((vel-80)*7))
else:
    print("Voce não ultrapassou o limite permitido!")
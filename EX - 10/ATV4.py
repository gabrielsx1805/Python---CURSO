km = float(input("Digite a KM que deseja viajar: "))

if km <= 200:
    print("O valor da viagem é: {}".format(0.5*km))
else:
    print("O valor da viagem é: {}".format(0.45*km))
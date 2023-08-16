import math
from math import sqrt,hypot

oposto = float(input("Digite o cateto oposto: "))
adjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = math.hypot(oposto,adjacente)
print("A soma dos catetos {:.2f} e {:.2f} é a hipotenusa {:.2f}".format(oposto,adjacente,hipotenusa))
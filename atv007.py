import math
angulo = float(input("Digite o Angulo desejado: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("SENO:{:.2f}   COSSENO:{:.2f}  TANGENTE:{:.2f}".format(seno,cosseno,tangente))
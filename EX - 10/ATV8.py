a = float(input("Digite o lado A em cm: "))
b = float(input("Digite o lado B em cm: "))
c = float(input("Digite o lado C em cm: "))

if a+b > c and a+c > b and c+b > a:
    print("é um triagulo")
else: 
    print("não é um triangulo!")
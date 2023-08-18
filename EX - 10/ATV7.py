salario = float(input("Digite seu salario: "))

if salario >= 1250.0:
    print("Seu novo salario, com acrescimo de 10% é: ",((salario * 10/100)+salario))
else:
    print("Seu novo salario, com acrescimo de 15% é: ",((salario * 15/100)+salario))
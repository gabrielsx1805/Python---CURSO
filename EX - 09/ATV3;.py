nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.lower()
nome3 = nome.find('santo')

if nome3 in [0]:
    print("A Palavra 'Santo' está no começo")
else:
    print("A Palavra'Santo' não está no começo")
 
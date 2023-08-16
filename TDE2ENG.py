def contagem():
    contagem_l = {}
    for letra in palavra:
        if letra in contagem_l:
            contagem_l[letra] += 1
        else:
            contagem_l[letra] = 1
            
    return contagem_l

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

contagem1 = contagem()

for letra in contagem1.items():
    print(f"{letra}")





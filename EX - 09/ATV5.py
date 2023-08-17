frase = input("Digite uma frase: ").strip()
frase = frase.lower()

print("A letra 'A' aparece: ",frase.count('a'),"vezes")
print("A primeira letra 'A' aparece na posição: ",frase.find('a')+1)
print("A ultima letra 'A' aparece na posição: ",frase.rfind('a')+1)
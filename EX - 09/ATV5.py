frase = input("Digite uma frase: ")
frase = frase.lower()

print("A letra 'A' aparece: ",frase.count('a'),"vezes")
print("A primeira letra 'A' aparece na posição: ",frase.find('a'))
print("A ultima letra 'A' aparece na posição: ",frase.rfind('a'))
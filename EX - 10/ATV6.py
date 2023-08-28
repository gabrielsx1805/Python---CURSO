a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

maior = a

if b > a and b>c:
    maior = b
if c > a and c > b:
    maior = c
    
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
    
    
print("O maior numero é: ",maior)
print("O menor numero é: ",menor)
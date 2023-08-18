a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a >= b and c:
    print(a, ' é o maior numero')
elif b >= a and c:
    print(b, ' é o maior numero')
elif c >= a and b:
    print(c, ' é o maior numero')


if a <= b and c:
    print(a, ' é o menor numero')
elif b <= c and a:
    print(b, ' é o menor numero')
elif c <= a and b:
    print(c, ' é o menor numero')
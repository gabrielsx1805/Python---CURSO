import random

pessoas = ['joao','maria','pedro','paulo']

nome = random.choice(pessoas)

print("O aluno escolhido foi: {}".format(nome))
ordem = random.shuffle(pessoas)
print(pessoas)
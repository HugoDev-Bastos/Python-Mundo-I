# o mesmo professor do desafio anterios quer sortear na ordem de apresentação de trabalhos dos alunos.
# Mostra nomes na ordem sorteado.
from random import shuffle
 
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordm de apresentação será:')
print(lista)

# Escreva um programa que faça o computador "Pensar" em um número de 0 a 5 e eça para o usuário tenta descpbrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se p usuário venceu ou perdeu.

from random import randint
from time import sleep

print("-=-"*20)
print(' Vou Pensar em um número entre 0 e 5. Tente adivinhar...')
print("-=-"*20)

computador = randint(0,5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if n == computador:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print('VOCÊ ERROU! Pensei no número {} e não no {}!'.format(computador, n))




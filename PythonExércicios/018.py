# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo.
from math import radians, cos, sin, tan

valor = float(input("Digite um Valor: "))

cose = cos(radians(valor))
seno = sin(radians(valor))
tang = tan(radians(valor))

print('='*50)
print("O valor em Seno é: {:.2f}".format(seno)) 
print("O valor em Cosseno é: {:.2f}".format(cose))
print("O valor da Tangente é: {:.2f}".format(tang))
print('='*50)



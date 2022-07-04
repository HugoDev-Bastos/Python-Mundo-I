# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triagulo retagulo. 
# Calacule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))

'''hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hi))'''

hi = hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hi))

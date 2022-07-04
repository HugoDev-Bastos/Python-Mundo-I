# Cier um programa que leia um número interiro e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2

if resultado == 0:
    print ("O resultado foi PAR")
else:
    print ("O resultado foi IMPAR")
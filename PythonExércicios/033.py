#Faça um programa que leia três número e mostre qual é o menor e qual e o maior.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceito número: "))

# Verificando que é o menor
menor = a
if b < a and b < c:
    menor = b
if c <  a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))

# Verificando quem é o Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))




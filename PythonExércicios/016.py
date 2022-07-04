#Crie um progama que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# o Número 6.127 tem a parte Interia 6.

'''from math import trunc

num = float(input("Digite um Valor: "))
print("O valor é {} é sua porção é {}.".format(num, trunc(num))) '''


num = float(input('Digite um Valor: '))
print('O valor é {} e a sua porção Inteira é {}.'.format(num, int(num)))

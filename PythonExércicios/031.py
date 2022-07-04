#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, vobrando R$0,50 po Km para viagens de até 200km e R$0,45 para viagens mais longas.


dis = int(input('Qual é a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {:0.1f}km'.format(dis))

"""
if dis <= 200:
    valor = dis * 0.50
    print("E o preço da sua passagem será de R${:0.2f}".format(valor))
else:
    valor2 = dis * 0.45
    print("E o preço da sua passagem será de R${:0.2f}".format(valor2))
"""

## Simplificado

preço = dis * 0.50 if dis <= 200 else dis *0.45
print("E o preço da sua passagem será de R${:0.2f}".format(preço))
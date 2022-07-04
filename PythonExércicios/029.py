# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostra dizendo que ele foi multado.
# A multa vai custar 7,00 por cada km acima do limite.

velocidade = int(input('Qual é a vlocidade atual do carro? '))

if velocidade > 80:

    multa = (velocidade - 80) * 7

    print('MULTADO! Você excedeu o limite permitido que é e 80Km/h')
    print('Você deverá pagar uma multa de R${}!'.format(multa))
    print('Tenha um bom dia! Dirija com Segurança!')
else:
    print('Tenha um bom dia! Dirija com Segurança!')
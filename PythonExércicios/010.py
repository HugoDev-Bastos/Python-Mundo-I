# Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos sólares ela pode comprar.
# us$1.00 = 3,27

print('='*50)

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.62
print('Com R${:.2f} você comprar US${:.2f}'.format(real, dolar))

print('='*50)
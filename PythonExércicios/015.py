# Calcule a quantidade de dias com uma diaria de R$60.
# Calcule a quantidade de Km rodados por R$0.15/Km.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantidade de Km rodado? '))

pago = dias * 60 + (km * 0.15)

print('O total a pagar é de R${:.2f}'.format(pago))

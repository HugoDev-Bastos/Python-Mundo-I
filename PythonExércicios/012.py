# faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pr =  float(input('Qual é o preço do produto? R$'))
desc = int(input('Qual a % do desconto? '))
novo = pr - (pr * desc /100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custa R${:.2f}'.format(pr, novo))
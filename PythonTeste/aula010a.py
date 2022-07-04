# Condições Simples e Compostas #

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2

'''
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruin! Estude mais!')
'''

## Condição Simplificada

print("A sua nota foi {:.1f}".format(m))
print("Parabéns" if m >= 6 else "Estude mais!")
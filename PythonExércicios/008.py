# Leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite um valor: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100 
mm = medida * 1000

print('='*20)
print('O valor em Metros é de {:.0f}'.format(medida))
print('Possui {} Km'.format(km))
print('Possui {} hm'.format(hm))
print('Possui {} dam'.format(dam))
print('Possui {:.0f} dm'.format(dm))
print('Possui {:.0f} cm'.format(cm))
print('Possui {:.0f} mm'.format(mm))
print('='*20)
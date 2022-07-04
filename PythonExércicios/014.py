# escreva um programa que coverta um atemperatura digitada em °C converta para °F.

c = float(input('Informe a temperatura em °C: '))
f = 9*c / 5+32 # segue a ordem de precedencia

print('A temperatura de {}°C corresponde a {}°F'.format(c,f))
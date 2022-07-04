# leia largura e a altura de uma parede em metros.
# calcule a sua área e a quantidade de tinta necessaria para pintá-la. 
# sabendo quea cada litro de tinta pinta uma area de 2m^2.

print('='*50)
la = float(input("Largura da parede: "))
al = float(input("Atura da parede: "))
ar = al * la
ti = ar / 10

print('='*50)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(al, la, ar))
print('Para pintar essa parede, você precisará de {:.1f}l de tinta'.format(ti))
print('='*50)
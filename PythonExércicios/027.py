n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

#print(nome)
print('Primeiro nome é: {}'.format(nome[0]))
print('Último nom é: {}'.format(nome[len(nome)-1]))

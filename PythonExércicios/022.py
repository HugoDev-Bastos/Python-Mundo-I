nome = str(input('Nome Completo: ')).strip()

print('Maiúsculas: {}'.format(nome.upper))
print('Minúsculas: {}'.format(nome.lower))
print('Seu nome tem ao todo{} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem letras {}'.format(separa[0], len(separa[0])))
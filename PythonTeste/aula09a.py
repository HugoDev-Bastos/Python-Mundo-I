
frase = 'Curso em Vídeo Python'

print('='*50)
print('Análises')
print('='*50)

print(frase[9::3])
print('len: ', len(frase))
print('coun: ',frase.count('o', 0, 13))
print('find (posisão do índice): ',frase.find('deo'))
print('find com -1: ',frase.find('android'))
print('in: ', 'Curso' in frase)

frase2 = 'Testando Novos Comandos'

print('='*50)
print('Transformação')
print('='*50)

print('replace: ', frase2.replace('Novos', 'Android')) #Faz a troca
print('upper: ', frase2.upper()) #Tudo em Maiúculos
print('lower: ',frase2.lower()) #Tudo em Minúsculo
print('capitalize: ',frase2.capitalize()) #Primeiro caracter em maiúsculo
print('title: ',frase2.title()) #Iniciais em Maiúsculos
print('strip: ',frase2.strip()) #Remove espaço Vazios
print('rstrip: ', frase2.rstrip()) #Remove espaços Vazios do lado direito
print('lstrip: ', frase2.lstrip()) #Remove espaços Vazios do lado Esquedo


print('='*50)
print(' Divisão')
print('='*50)

print(frase.split())
print(''.join(frase))

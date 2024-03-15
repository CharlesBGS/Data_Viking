# Determine se uma letra inserida pelo usuário é uma vogal ou consoante.
# Armazene as vogais em uma lista e implemente sua solução.
# Desconsidere a possibilidade de o usuário inserir números ou caracteres especiais.

vogais = ['a', 'e', 'i', 'o', 'u']

caractere = input('Digite uma letra para saber se ela é uma vogal ou consoante: \n').lower()

if caractere in vogais:
    print(f'o caractere {caractere} é uma Vogal')
else:
    print(f'O caractere {caractere} é uma consoante.')

'''
# Solução apresentada pelo prof. Odemir:

letra=input('Digite uma letra: ')
vogais=['a','e','i','o','u']
if letra in vogais:
    print('A letra digitada é uma vogal.')
else:
    print('A letra digitada é uma consoante.')

'''
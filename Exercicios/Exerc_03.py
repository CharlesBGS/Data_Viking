# Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome
# completo do usuário na tela.

nome = input('Digite seu nome: ').strip().title()
sobrenome = input('Digite seu sobrenome: ').strip().title()
print(f'Seu nome completo é {nome} {sobrenome}')

# O método .strip() serve para remover espaços em branco antes e depois do que foi digitado pelo usuário.
# O método .title() serve para transformar a primeira letra do que foi digitado em maiúscula.
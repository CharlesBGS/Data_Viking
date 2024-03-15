# Escreva um programa que peça o nome e a idade do usuário.

# Caso a idade do usuário seja maior ou igual a 18 anos:
# apresente a seguinte mensagem: "Seja bem-vindo ao nosso site [nome]!";

# caso contrário, apresente a seguinte mensagem:
# "Você não pode acessar nosso site [nome].".

nome = input('Digite seu nome: \n').strip().title()
idade = int(input('Digite sua idade: \n'))

if idade >= 18:
    print(f'Seja bem-vindo ao nosso site {nome}!')

else:
    print(f'Você não pode acessar nosso site {nome}.')

'''
# Solução apresentada pelo prof. Odemir:
# Novamente ele aplicou .strip() e .title() na string formatada., enquanto eu o fiz diretamente na variável.

nome=input('Digite seu nome: ')
idade=int(input('Digite sua idade: '))
if idade>=18:
    print(f'Seja bem-vindo ao nosso site {nome.strip().title()}.')
else:
    print(f'Você não pode acessar nosso site {nome.strip().title()}.')

'''
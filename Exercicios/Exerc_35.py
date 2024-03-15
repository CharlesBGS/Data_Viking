# Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário.
# Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida
# (número entre 1 e 10) mostre na tela uma mensagem personalizada.

tabela_categoria = {
    1: '$ 0,5',
    2: '$ 11,3',
    3: '$ 17,5',
    4: '$ 33,97',
    5: '$ 103,47',
    6: '$ 44,67',
    7: '$ 12,55',
    8: '$ 14,87',
    9: '$ 98,12',
    10: '$ 131,4'
}

consulta = int(input('Digite um número inteiro de 1 a 10 equivalente a categoria que deseja consultar o valor: \n'))

if consulta in tabela_categoria:
    print(f'O valor registrado para a categoria {consulta} é de {tabela_categoria[consulta]}')
else:
    print(f'O valor {consulta} não é uma categoria válida. Digite um número inteiro de 1 a 10.')


'''
# Solução apresentada pelo prof. Odemir:

# Ele fez uso de laços de repetição.



categoria=int(input('Digite a categoria do produto: '))
if categoria==1:
    print('O preço do produto é: $ 0.5')
elif categoria==2:
    print('O preço do produto é: $ 11.3')
elif categoria==3:
    print('O preço do produto é: $ 17.5')
elif categoria==4:
    print('O preço do produto é: $ 33.97')
elif categoria==5:
    print('O preço do produto é: $ 103.47')
elif categoria==6:
    print('O preço do produto é: $ 44.67')
elif categoria==7:
    print('O preço do produto é: $ 12.55')
elif categoria==8:
    print('O preço do produto é: $ 14.87')
elif categoria==9:
    print('O preço do produto é: $ 98.12')
elif categoria==10:
    print('O preço do produto é: $ 131.4')
else:
    print('Opção inválida.')


'''


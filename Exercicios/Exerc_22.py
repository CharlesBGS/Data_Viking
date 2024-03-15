# Faça um programa que peça uma string ao usuário e mostre na tela a quantidade de caracteres.
#
# Dica: use a função built-in len() e trate a string com o método strip().

frase = str(input('Digite uma frase para saber quantos caracteres ela possui: \n'))
frase = frase.strip()

print(f'A frase digitada foi: {frase}')
print(f'E possui {len(frase)} caracteres.')

# Obs: O método .strip() remove espaços do início e do fim da string, e não os que estiverem entre caracteres.

'''
# Solução apresentada pelo prof. Odemir:
# Engraçado ele ter esquecido de tratar a string :)


string=input('Digite algo: ')
print(f'Você digitou: {string}')
print(f'Quantidade de caracteres do que você digitou é: {len(string)}')


'''
# Escreva um programa que inverta uma string. Exemplos:

# Hello World!
# Python
# !dlroW olleH
# nohtyP

frase1 = input('Digite um texto: \n')
frase2 = input('Digite um texto: \n')

print(f'{frase1[::-1]}')
print(f'{frase2[::-1]}')

# Uma string se comporta como uma lista, então é possivel percorrer os itens da lista navegando
# pelos seus respectivos indices. Sendo assim, frase1[::-1] corresponde a string de seu início (primeiro ':') que
# poderia ser substituido pelo valor do indice pelo qual se deseja iniciar, ao fim (segundo ':') que se comporta
# da mesma forma que o início, e em ordem invertida (representada pelo -1).

'''
# Solução apresentada pelo prof. Odemir:

string1='Hello World!'
string2='Python'
print(string1)
print(string2)
print(string1[::-1])
print(string2[::-1])

'''
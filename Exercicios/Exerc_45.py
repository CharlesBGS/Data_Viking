# Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.


# Minha primeira solução:
# Não está errada, mas não era a resposta esperada, sem dúvidas rs
'''
for i in range(21):
    print(i*5)
'''

# após ver a solução do prof.:

lista = [] # lista vazia que será preenchida com números divisíveis por 5.
x = 1 # número inicial a partir do qual iremos iterar

while len(lista)<20: # continuará enquanto o comprimento da lista for menor que 20.
    if x % 5 == 0: # Verifica se 'x' é divisível por 5. Se for, ele é adicionado à lista.
        lista.append(x)
        x+=1 # 'x' é incrementado em 1 para passar para o próximo número.
    x+=1 # garante que 'x' seja incrementado, mesmo se o número não for divisível por 5.

# Após o preenchimento da lista, este loop for itera sobre cada elemento num na lista e imprime-o na tela.
for num in lista:
    print(num)
'''
# Solução apresentada pelo prof. Odemir:

lista=[]
x=1
#armazenando os números em uma lista
while len(lista)<20:
    if x%5==0:
        lista.append(x)
        x+=1
    x+=1

#mostrando os números na tela
for num in lista:
    print(num)

'''
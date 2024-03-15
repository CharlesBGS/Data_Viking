# Modifique o programa anterior e permita que o usuário especifique o ano e o mês a serem mostrados na tela.

import calendar

ano = int(input('Digite um ano: '))
mes = int(input('Digite um mês: '))

print(calendar.month(ano,mes))


'''
# Solução apresentada pelo prof. Odemir:

import calendar
ano=int(input('Ano: '))
mes=int(input('Mês: '))

print(calendar.month(ano,mes))


'''
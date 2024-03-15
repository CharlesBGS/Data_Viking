# Elabore um progama para verificar se um ano é bissexto ou não.

# A condição para ser um ano bissexto é: o ano deve ser divisível por 400;

# ou se for divisível por 4 e não for divisível por 100.


# Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# O ano é bissexto (tem 366 dias).
# O ano não é um ano bissexto (tem 365 dias).

ano = int(input('Digite um ano para verificar se é ou não um ano bissexto: \n'))

# if ano%400==0 or (ano%4==0 and not ano%100==0):
#   Solução do prof. Odemir.

if ano%4 == 0 or ano%100 == 0 and ano%400 == 0:
    print(f'O ano {ano} é um ano bissexto.')
else:
    print(f'O ano {ano} não é um ano bissexto.')


'''
# Solução apresentada pelo prof. Odemir:
# Interessante a solução do prof. Ele usou a condição 'and not', fazendo valer a descrição do problema.
# se P ou se Q e não R, então Verdadeiro.

ano=int(input('Ano : '))
if ano%400==0 or (ano%4==0 and not ano%100==0):
    print('Ano bissexto.')
else:
    print('Ano não bissexto.')

'''
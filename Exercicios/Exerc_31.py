# Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.
# 13/12/2022 - 19:28:07

import datetime

data = datetime.datetime.now()

print(data.strftime('%d/%m/%y - %H:%M:%S'))
# o trecho '%H:%M:%S' precisa ser feito em letras maiúsculas


'''
# Solução apresentada pelo prof. Odemir:

import datetime

data_atual=datetime.datetime.now()
print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))

'''
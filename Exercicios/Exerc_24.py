# O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa.

# Escreva um programa que peça o nome, a idade , o peso e a altura do usuário.

# Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.

# IMC<17 - Muito abaixo do peso ideal
# 17<=IMC<18,5 - Abaixo do peso
# 18,5<=IMC<25 - Peso normal
# 25<=IMC<30 - Acima do peso
# 30<=IMC<35 - Obesidade I
# 35<=IMC<40 - Obesidade II (severa)
# IMC>=40 - Obesidade III (mórbida)
# Lembre que: IMC=massa/(altura*altura)

# Fonte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal

print('Para saber seu IMC será necessário informar alguns dados.')
print('O cálculo do IMC é feito por meio da equação: IMC=massa/(altura*altura')
nome = input('Digite seu nome: ').strip().title()
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso/(altura*altura)

if IMC<17 :
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Muito abaixo do peso ideal')
# IMC<17 - Muito abaixo do peso ideal

elif IMC <= 17 and IMC<18.5:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Abaixo do peso')
# 17<=IMC<18,5 - Abaixo do peso

elif IMC <= 18.5 and IMC<25:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Peso normal')
# 18,5<=IMC<25 - Peso normal

elif IMC <= 25 and IMC<30:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Acima do peso')
# 25<=IMC<30 - Acima do peso

elif IMC <= 30 and IMC<35:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Obesidade I')
# 30<=IMC<35 - Obesidade I

elif IMC <= 35 and IMC<40:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Obesidade II (severa)')
# 35<=IMC<40 - Obesidade II (severa)

elif IMC>=40:
    print(f'Olá {nome}, seu IMC é de {IMC:.2f} e você tem a seguinte classificação: Obesidade III (mórbida')
# IMC>=40 - Obesidade III (mórbida)


'''
# Solução apresentada pelo prof. Odemir:
# interessante como ele fez a verificação: '17<=imc<18.5'.
# Novamente ele esqueceu de atender a todos as solicitações do enunciado :)


print('Cálculo do IMC')
altura=float(input('Insira sua altura : \n'))
peso=float(input('Insira seu peso : \n'))
imc=peso/(altura*altura)  #poderíamos fazer peso/altura**2
print('Processando seus dados...')
if imc<17:
    print('Muito abaixo do peso.')
elif 17<=imc<18.5:
    print('Abaixo do peso.')
elif 18.5<=imc<25:
    print('Peso normal.')
elif 25<=imc<30:
    print('Acima do peso.')
elif 30<=imc<35:
    print('Obesidade Grau I.')
elif 35<=imc<40:
    print('Obesidade Grau II (severa).')
else:
    print('Obesidade Grau III (mórbida).')

'''
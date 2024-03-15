# Resolva o exercício anterior para as categorias de 1 a 8. Utilize estruturas aninhadas.

categoria=int(input('Digite a categoria do produto: '))

if categoria==1:
    print('O preço do produto é: $ 0.5')
else:
    if categoria==2:
        print('O preço do produto é: $ 11.3')
    else:
        if categoria==3:
            print('O preço do produto é: $ 17.5')
        else:
            if categoria==4:
                print('O preço do produto é: $ 33.97')
            else:
                if categoria==5:
                    print('O preço do produto é: $ 103.47')
                else:
                    if categoria==6:
                        print('O preço do produto é: $ 44.67')
                    else:
                        if categoria==7:
                            print('O preço do produto é: $ 12.55')
                        else:
                            if categoria==8:
                                print('O preço do produto é: $ 14.87')
                            else:
                                if categoria==9:
                                    print('O preço do produto é: $ 98.12')
                                else:
                                    if categoria==10:
                                        print('O preço do produto é: $ 131.4')
                                    else:
                                        print('Opção inválida.')


'''
# Solução apresentada pelo prof. Odemir:
# Como eu havia resolvido a questão anterior com o uso de dicionário, copiei a resposta do prof. do exercício 35, e
# alteirei o código para que ficasse aninhado.


categoria=int(input('Categoria do produto: '))
if categoria==1:
    print('Preço: $ 0.5')
else:
    if categoria==2:
        print('Preço: $ 11.35')
    else:
        if categoria==3:
            print('Preço: $ 17.5')
        else:
            if categoria==4:
                print('Preço: $ 33.97')
            else:
                if categoria==5:
                    print('Preço: $ 103.47')
                else:
                    if categoria==6:
                        print('Preço: $ 44.67')
                    else:
                        if categoria==7:
                            print('Preço: $ 12.55')
                        else:
                            if categoria==8:
                                print('Preço: $ 14.87')
                            else:
                                print('Categoria inválida.')

'''
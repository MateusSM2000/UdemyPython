caminho_arquivo = 'C:\\Users\\User\\PycharmProjects\\186.txt'

#quando abre um arquivo no python ele coloca como se fosse um cursor no arquivo e para os métodos de ler e escrever, o cursor precisa estar na posição correta para funcionar
#o metodo seek faz justamente isso, move o cursor para o local desejado; arquivo.seek(0, 0) move para o inicio
#quando um arquivo é aberto o cursor automaticamente é movido para o inicio

#o modo 'a' é como se fosse um append, ele adiciona ao arquivo. Já o 'w' ele apaga td q já tem no arquivo e escreve
#colocar parâmetro encoding= 'utf8' para escrever caracteres como 'ç' e acentos normalmente no arquivo

with open(caminho_arquivo,'w+', encoding= 'utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4'))

    arquivo.seek(0,0)
    print(arquivo.read())
    print('')

    print(arquivo.seek(0,0))
    print(arquivo.readline(), end= '')
    print(arquivo.readline(), end= '')
    print(arquivo.readline(), end='')
    print(arquivo.readline())
    print('')

    print(arquivo.seek(0,0))
    for linha in arquivo.readlines():
        print(linha, end = '')

#os.remove(caminho_arquivo) e os.unlink(caminho_arquivo) deletam o arquivo
#os.rename(caminho_arquivo, novo_caminho_arquivo) renomeia o arquivo e/ou move para outro lugar
import os

print(__file__)
print()

caminho = os.path.join('/Users','User','PycharmProjects', 'teste.txt')

print(caminho)
with open(caminho, 'w', encoding='utf8') as arquivo:
    arquivo.write('a')
print()

print(os.path.split(caminho))
caminho2, arquivo = os.path.split(caminho)
print(caminho2, arquivo)
print(os.path.splitext(arquivo))
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo, extensao_arquivo)
print()

print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(os.path.abspath('.')))
print(os.path.dirname(os.path.abspath('.')))
print(os.path.dirname(caminho))
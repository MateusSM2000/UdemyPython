import os

caminho = r'C:\Users\User\PycharmProjects'

print(os.listdir(caminho))

lista = []
for diretorio in os.listdir(caminho):
    diretorio_completo = os.path.join(caminho, diretorio)
    if os.path.isdir(diretorio_completo):
        print(diretorio)
        lista.append(diretorio_completo)

for diretorio in lista:
    print(os.listdir(diretorio))
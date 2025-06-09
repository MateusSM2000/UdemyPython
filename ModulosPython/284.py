import os

caminho = r'C:\Users\User\PycharmProjects'

print(os.walk(caminho))
print()

for pasta_atual, diretorios, arquivos in os.walk(caminho):
    print(f'Pasta atual: {pasta_atual}\n'
          f'Arquivos da pasta: {arquivos}\n'
          f'Diretórios da pasta: {diretorios}\n'
          )
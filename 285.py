import os

def formata_tamanho(tamanho_arquivo:int):
    if tamanho_arquivo / 1000000000 >= 1:
        return f'{tamanho_arquivo / 1000000000:.3f} GB'
    if tamanho_arquivo / 1000000 >= 1:
        return f'{tamanho_arquivo / 1000000:.3f} MB'
    if tamanho_arquivo / 1000 >= 1:
        return f'{tamanho_arquivo / 1000:.3f} KB'
    else:
        return f'{tamanho_arquivo} Bytes'

caminho = r'C:\Users\User\PycharmProjects'

tamanho_total_caminho = 0
for pasta_atual, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta_atual, arquivo)
        tamanho_total_caminho += os.path.getsize(caminho_arquivo)

print(formata_tamanho(tamanho_total_caminho))
print(os.path.getsize(caminho))
print(os.stat(caminho))
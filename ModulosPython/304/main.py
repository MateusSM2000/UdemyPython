import os
from pathlib import Path
from zipfile import ZipFile

caminho_raiz = Path(__file__).parent
caminho_diretorio_zip = caminho_raiz / 'aula304_compactado'
caminho_compactado = caminho_diretorio_zip / 'aula304_compactado.zip'
caminho_descompactado = caminho_diretorio_zip / 'aula304_descompactado'

caminho_diretorio_zip.mkdir(exist_ok=True)

def criar_arquivos(qtd:int, caminho_dir:Path) -> None:
    for n in range(1, qtd+1):
        with open(caminho_dir / f'arquivo{n}.txt', 'w', encoding='utf8') as arquivo:
            arquivo.write(f'arquivo{n}\n')


criar_arquivos(4, caminho_diretorio_zip)

with ZipFile(caminho_compactado, 'w') as zip_:
    for pasta_atual, diretorios, arquivos in os.walk(caminho_diretorio_zip):
        for arquivo in arquivos:
            if caminho_compactado == Path(pasta_atual) / arquivo:
                continue
            else:
                zip_.write(Path(pasta_atual) / arquivo, arquivo)

with ZipFile(caminho_compactado, 'r') as zip_:
    for arquivo in zip_.namelist():
        print(arquivo)

with ZipFile(caminho_compactado, 'r') as zip_:
    zip_.extractall(caminho_descompactado)
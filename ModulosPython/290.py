from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(caminho_projeto.absolute())
print()

caminho_arquivo = __file__
print(caminho_arquivo)
print()

caminho_arquivo2 = Path(__file__)
print(caminho_arquivo2)
print(caminho_arquivo2.parent)
print(caminho_arquivo2.parent.parent)
print(caminho_arquivo2.parent.parent / 'Nova_Pasta')
print()

print(Path.home())
caminho_pasta = Path.home() / 'Desktop' / 'Nova_Pasta'
caminho_pasta.mkdir(exist_ok=True)
caminho_arquivo = caminho_pasta / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá mundo')
with caminho_arquivo.open('a', encoding='utf8') as file:
    file.write('\nNova linha')
print(caminho_arquivo.read_text())
#rmtree(caminho_pasta)
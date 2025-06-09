import csv
from pathlib import Path

caminho_csv = Path(__file__).parent / 'Pasta1.CSV'

with open(caminho_csv, 'r', encoding='utf8') as arquivo:
    lista = csv.reader(arquivo)
    print(lista)
    print(list(lista))
    print()

with open(caminho_csv, 'r', encoding='utf8') as arquivo:
    lista = csv.DictReader(arquivo)
    print(lista)
    print(list(lista))
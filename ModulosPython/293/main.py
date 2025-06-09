import csv
from pathlib import Path

lista = [{'Nome': 'Mateus Schmidt Mesquita', 'Idade': '24', 'Endereço': 'Rua Boa Morte, 260, Apto 141, Centro, Limeira-SP'},
         {'Nome': 'Gabriele Borges', 'Idade': '21', 'Endereço': 'Rua 4PF, 47, Jardim Kennedy, Rio Claro-SP'}
         ]

caminho_csv = Path(__file__).parent / 'Pasta2.csv'

with open(caminho_csv, 'w', encoding='utf8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(lista[0].keys())
    for linha in lista:
        escritor.writerow(linha.values())
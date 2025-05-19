from string import Template
from pathlib import Path

dados = {
    'cliente': 'Mateus Schmidt Mesquita',
    'data': '27/05/2027',
    'valor': 'R$127.98',
    'email': 'contato@megamisto.com',
    'telefone': '+55 19 3441-1490',
    'empresa': 'MegaMisto'
}

caminho_texto = Path(__file__).parent / 'texto'

with open(caminho_texto, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    print(Template(texto).substitute(dados))
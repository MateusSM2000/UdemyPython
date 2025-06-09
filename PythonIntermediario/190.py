import json

#o json serve para salvar dados de dicionarios ou listas em outros arquivos sem perder sua classe de dicionario lista, ou seja, se quiser importar de um arquivo json,
#um dicionario tupla ou lista, para o python, ele nao vai perder sua classe (tuplas o json transforma em lista)

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

#ensure_ascii desabilita o ascii e deixa rodar o encoding q quiser
#indent formata visualmente em linhas no arquivo a fim de melhor visualização
with open('190.json', 'w+', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii= False, indent= 2)
    arquivo.seek(0,0)
    pessoa = json.load(arquivo)
    print(type(pessoa))
    print(pessoa)
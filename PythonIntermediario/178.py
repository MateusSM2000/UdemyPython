import functools

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

help(functools.reduce)
total = functools.reduce(lambda acumulador, p: acumulador + p['preco'], produtos, 0)
print(total)

total = 0
for p in produtos:
    total = total + p['preco']
print(total)
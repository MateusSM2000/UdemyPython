import itertools

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


#groupby(iterable, key=None)
 #
 # make an iterator that returns consecutive keys and groups from the iterable
 #
 #  iterable
 #   Elements to divide into groups according to the key function.
 # key
 #   A function for computing the group category for each element.
 #   If the key function is not specified or is None, the element itself
 #    is used for grouping.

alunos_ordenados = sorted(alunos, key= lambda a: a['nota'])
print(alunos_ordenados)
print('\n\n')

notas_agrupadas = itertools.groupby(alunos_ordenados,key= lambda a: a['nota'])
print(notas_agrupadas)
print(list(notas_agrupadas))

print('\n\n\n')

notas_agrupadas = itertools.groupby(alunos_ordenados,key= lambda a: a['nota'])

for chave, grupo in notas_agrupadas:
    print(chave)
    for aluno in grupo:
        print(aluno)


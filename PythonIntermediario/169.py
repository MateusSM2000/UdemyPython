# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import itertools

nomes = ['Mateus', 'Gabriele', 'dsadsadsadsa']
sobrenomes = ['Schmidt Mesquita', 'Borges']


nome_sobrenome = [(nomes[i], sobrenomes[i])
                  for i in range(min(len(nomes), len(sobrenomes)))
                 ]
print(nome_sobrenome)


print(list(zip(nomes, sobrenomes)))


print(list(itertools.zip_longest(nomes, sobrenomes)))



print(list(itertools.zip_longest(nomes, sobrenomes, fillvalue='sem nome')))
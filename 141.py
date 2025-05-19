lista = [('nome', 'Mateus'),
         ('idade', 24),
         ('altura', 1.83),
         ('cor', 'branco')
         ]


dicionario = {chave: valor
              for chave, valor in lista
              #if valor == 'Mateus' or valor == 24
              }
print(dicionario)



print(dict(lista))
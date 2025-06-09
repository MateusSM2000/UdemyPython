lista1 = []
for x in range(1, 4):
    for y in range(1, 4):
        lista1.append((x, y))
print(lista1)


lista2 = [(x, y)
          for x in range(1, 4)
          for y in range(1, 4)
          ]
print(lista2)


lista3 = [[letra for letra in 'Mateus']]
print(lista3)


lista4 = []
listaaux = []
for letra in 'Mateus':
    listaaux.append(letra)
lista4.append(listaaux)
print(lista4)
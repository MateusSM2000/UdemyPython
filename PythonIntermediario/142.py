lista = ['a',
         'b',
         'c',
         1,
         1.3,
         'd',
         2.5]
print(lista)
a = 0
for v in lista:
    if isinstance(v, str):
        lista[a] = v.upper()
    if isinstance(v, (int, float)):
        lista[a] = v * 2
    a = a + 1
print(lista)
import itertools

#combinaçao: (x,y) e (y,x) agrupa só 1
#permutaçao: (x,y) e (y,x) agrupa os dois

nomes = ['Mateus','Gabriele','Márcia','Jaqueline']

print(itertools.combinations(nomes,2))
print('combinação em 2:',list(itertools.combinations(nomes,2)))
print('combinação em 3:',list(itertools.combinations(nomes,3)))
print('combinação em 4:',list(itertools.combinations(nomes,4)))
print('permutação em 2:',list(itertools.permutations(nomes,2)))
print('permutação em 3:',list(itertools.permutations(nomes,3)))
print('\n\n\n')

#product: faz como se fosse uma multiplicação de dois parenteses com listas; [x , y] , [a , b] retorna (x , a), (x , b), (y , a), (y , b)

camisetas = [
             ['preta', 'branca'],
             ['p', 'm', 'g'],
             ['algodão', 'poliéster']
             ]

print(itertools.product(*camisetas))
print(*list(itertools.product(*camisetas)), sep= '\n')
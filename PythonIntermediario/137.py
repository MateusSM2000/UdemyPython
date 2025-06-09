produtos = [{'nome': 'banana', 'preço': 1},
            {'nome': 'açaí' ,'preço': 2},
            {'nome': 'maçã', 'preço': 3}
            ]

novos_produtos = [{**produto, 'preço':produto['preço']*2}
                  if produto['preço'] >= 2 else {**produto}
                  for produto in produtos]
print(novos_produtos)



novos_produtos = produtos.copy()
for p in novos_produtos:
    if p['preço'] >= 2:
        p['preço'] = p['preço']* 2
print(novos_produtos)
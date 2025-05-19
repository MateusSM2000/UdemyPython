import functools

produtos = [{'nome': 'Produto 4', 'preço': 100},
            {'nome': 'Produto 2', 'preço': 95.44},
            {'nome': 'Produto 1', 'preço': 23.89},
            {'nome': 'Produto 5', 'preço': 89},
            {'nome': 'Produto 3', 'preço': 45}
            ]

def aumento_porcentagem1(porcentagem):
    def decorador(valor):
        return valor * porcentagem
    return decorador

aumentar_dez_porcento = aumento_porcentagem1(1.1)


novos_preços = [{**produto, 'preço': aumentar_dez_porcento(produto['preço'])}
                for produto in produtos]
print(novos_preços)


#já aprendemos como fazer oq foi feito acima anteriormente. Agr outro jeito de fazer a msm coisa


def aumento_porcentagem2(valor, porcentagem):
    return valor * porcentagem

aumentar_dez_porcento = functools.partial(aumento_porcentagem2, porcentagem= 1.1)
novos_preços = [{**produto, 'preço': aumentar_dez_porcento(produto['preço'])}
                for produto in produtos]
print(novos_preços)

#ou seja esse partial() cria automaticamente pra vc a sub funçao decoradora


print('\n\n\n')


#agr vamos ver uma função do python que faz a msm coisa do list comprehension no exemplo novos_preços = [{**produto, 'preço': aumentar_dez_porcento(produto['preço'])}
#                                                                                                         for produto in produtos]


def mudar_preço(produto):
    return {**produto, 'preço': aumentar_dez_porcento(produto['preço'])}

novos_preços = map(mudar_preço, produtos)
print(novos_preços)
print(list(novos_preços))

#ou seja, esse map faz o for pra vc. Outro exemplo abaixo:

print('\n\n\n')
print(list(map(lambda  x: x * 3, [1, 2, 3, 4])))
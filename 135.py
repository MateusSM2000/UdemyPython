pessoa = {'nome':'Mateus', 'sobrenome':'Schmidt Mesquita'}
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

a, b = pessoa.keys()
print(a, b)

a, b = pessoa.values()
print(a, b)

for a in pessoa.values():
    print(a)

for a in pessoa.keys():
    print(a)

for a, b in pessoa.items():
    print(a, b)


dados = {'altura':1.83, 'peso':92}
(a1, a2), (b1, b2) = dados.items()
pessoa[a1] = a2
pessoa[b1] = b2
print(pessoa)



#asterisco empacota ou desempacota. Um asterisco para tupla, e dois asteriscos para dicionario
pessoa1 = {'nome':'Mateus', 'sobrenome':'Schmidt Mesquita'}
dados1 = {'altura':1.83, 'peso':92}
pessoa_completa = {**pessoa1, **dados1}
print(pessoa_completa)



def mostrar_argumentos(*valor, **chave_e_valor):
    print(f'valor: {valor}\nchave e valor: {chave_e_valor}')
config = ['opção1', 'opção2', 'opção3']
menu = {'config1':'opção1',
        'config2':'opção2',
        'config3':'opção3'
        }
mostrar_argumentos(*config, **menu)

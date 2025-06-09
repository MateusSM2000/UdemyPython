#inverte_string é jogada como parametro para a funcao crian_funcao, q é executada primeiramente, e inverte_string só é executado quando chamado (escrito com parenteses no final)

def criar_funcao(func):
    print('Iniciando decorador...')
    print(func)
    def decorador(palavra):
        print('Função decorada!')
        print(palavra)
        return func(palavra)
    return decorador

@criar_funcao
def inverte_string(string):
    print('Iniciando inverte_string...')
    print('FIM inverte_string')
    return string[::-1]


invertida = inverte_string('Mateus')
print(invertida)
print()
print()
print()


#executa a função externa apenas uma vez, e tbm guarda os objetos da função externa quando executada novamente
def a(func):
    lista = []
    print('aaaaaaaa')
    def c():
        lista.append(1)
        print(lista)
    return c


@a
def b():
    pass

b()
b()
b()
print()
print()
print()



def decoradora(func, lista=[]):
    def adc_lista_():
        func(lista)
        print(lista)
        return decoradora, lista
    return adc_lista_()

def adc_lista(lista):
    lista.append(1)

trial1, lista = decoradora(adc_lista)
trial2, lista = trial1(adc_lista, lista)
trial3, lista = trial2(adc_lista, lista)
trial4 = trial3(adc_lista, lista)
class A:
    def __init__(self, valor):
        self.atributo_a = valor


class B(A):
    def __init__(self,valor, valor2):
        super().__init__(valor)   #ou seja ele joga o valor para o parametro do init da classe A. Precisa so super().__init__(parametros_do_init_da_classe_mae) para
                                  #o def __init__(self) de subclasses funcionarem
        self.atributo_b = valor2


b = B('a', 'b')
print(b.atributo_a)
print(b.atributo_b)
#super(nome_classe_abaixo_da_q_vai_ser_usada, self).nome_atributo_ou_metodo faz usar o atributo ou metodo de msm nome da classe mãe
#se o parenteses estiver vazio, ele vai automaticamente fazer colocando no parenteses a classe em q o super esta sendo executado

class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')


class B(A):
    atributo_a = 'valor b'
    def metodo(self):
        print('B')


class C(B):
    atributo_a = 'valor c'
    def metodo(self):
        print(super(B,self).atributo_a)
        super(B,self).metodo()
        super().metodo()
        print('C')


c = C()
c.metodo()
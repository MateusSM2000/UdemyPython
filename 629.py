#o design pattern façade serve para facilitar o uso de um sistema de classes, no qual apenas utilizando do objeto do façade ele já executa os codigos necessarios,
# de uma maneira mais sucinta, para que o sistema funcione

class Class1:
    @staticmethod
    def set_config():
        print(f'Object from Class1 configured.')


class Class2:
    @staticmethod
    def set_config():
        print(f'Object from Class2 configured.')


class Class3:
    @staticmethod
    def set_config():
        print(f'Object from Class3 configured.')


class Class4:
    @staticmethod
    def set_config():
        print(f'Object from Class4 configured.')


class Facade:
    def __init__(self):
        self.class1 = Class1()
        self.class2 = Class2()
        self.class3 = Class3()
        self.class4 = Class4()

        self.class1.set_config()
        self.class2.set_config()
        self.class3.set_config()
        self.class4.set_config()



f = Facade()
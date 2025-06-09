#tem como criar instancias com atributos, com a classe, definidos nos parenteses durante a criação sem colocar os parametros nos parenteses do __init__, com @classmethod

class Connection:
    def __init__(self,host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password, host = 'localhost'):
        connection = cls(host)
        connection.user = user
        connection.password = password
        return connection


c1= Connection()
c1.set_user('Mateus')
c1.set_password('1234')
print(c1.__dict__)
print()

c2 = Connection.create_with_auth('Gabriele','2706', 'RioClaro')
print(c2.__dict__)
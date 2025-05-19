# a seguir, metodos dunder para habilitar operações matemáticas entre instancias
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


from math import sqrt

class Ponto:
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z
        if z is None:
            self.d = '2d'
        else:
            self.d = '3d'

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r}, d={self.d!r})'

    def __add__(self, other):
        if self.z is None and other.z is not None:
            return Ponto(self.x + other.x, self.y + other.y, other.z)
        elif self.z is not None and other.z is None:
            return Ponto(self.x + other.x, self.y + other.y, self.z)
        else:
            try:
                return Ponto(self.x + other.x, self.y + other.y, self.z + other.z)
            except TypeError:
                return Ponto(self.x + other.x, self.y + other.y)

    def __gt__(self, other):
        try:
            distancia_instancia1 = sqrt(self.x**2 + self.y**2 + self.z**2)
        except TypeError:
            distancia_instancia1 = sqrt(self.x**2 + self.y**2)
        try:
            distancia_instancia2 = sqrt(other.x**2 + other.y**2 + other.z**2)
        except TypeError:
            distancia_instancia2 = sqrt(other.x**2 + other.y**2)
        print(distancia_instancia1, distancia_instancia2)
        return distancia_instancia1 > distancia_instancia2




p1 = Ponto(1, 2)
p2 = Ponto(1, 2, 3)
p3 = Ponto(2, 3, 5)
p4 = Ponto(5, 7)

p5 = p1 + p2
p6 = p2 + p3
p7 = p1 + p4
p8 = p3 + p4
print(p5)
print(p6)
print(p7)
print(p8)
print('\n\n')


print(p1, p2, p1>p2)
print(p2, p3, p2>p3)
print(p1, p4, p1>p4)
print(p3, p4, p3>p4)
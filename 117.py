def criar_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar



duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
quintuplicar = criar_multiplicador(5)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))
print(quintuplicar(10))
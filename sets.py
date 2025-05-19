#Crie uma função que encontra o primeiro duplicado considerando o segundo
#número como a duplicação. Retorne a duplicação considerada.
#Requisitos:
#    A ordem do número duplicado é considerada a partir da segunda
#    ocorrência do número, ou seja, o número duplicado em si.
#    Exemplo:
#        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#    Se não encontrar duplicados na lista, retorne -1
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [9, 1, 8, 9, 9, 7, 2, 1, 6, 8]
l3 = [1, 3, 2, 2, 8, 6, 5, 9, 6, 7]
l4 = [3, 8, 2, 8, 6, 7, 7, 3, 1, 9]
l5 = [4, 8, 8, 5, 8, 1, 10, 3, 1, 7]
l6 = [1, 3, 7, 2, 2, 1, 5, 1, 9, 9]
l7 = [10, 2, 2, 1, 3, 5, 10, 5, 10, 1]
l8 = [1, 6, 1, 5, 1, 1, 1, 4, 7, 3]
l9 = [1, 3, 7, 1, 10, 5, 9, 2, 5, 7]
l10= [4, 7, 6, 5, 2, 9, 2, 1, 2, 1]
l11= [5, 3, 1, 8, 5, 7, 1, 8, 8, 7]
l12= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def duplicado(a):
    print(a)
    ListaIndex = []
    NumerosUnicos = set(a)
    print(NumerosUnicos)
    for b in NumerosUnicos:
        try:
            ListaAux = [b]
            ListaAux.append(a.index(b))
            SegundaOcorrencia = a.index(b) + 1
            ListaAux.append(a.index(b, SegundaOcorrencia))
        except ValueError:
            ListaIndex.append(ListaAux[:])
        else:
            ListaIndex.append(ListaAux[:])
    print(ListaIndex)
    NumerosRepetidos = []
    c = 0
    for b in ListaIndex:
        if len(b) > 2:
            NumerosRepetidos.append(ListaIndex[c][0])
        c = c +1
    print(NumerosRepetidos)
    if not bool(NumerosRepetidos):
        return -1
    cont = 0
    for c in range(0, len(ListaIndex)):
       for b in NumerosRepetidos:
          if b == a[c]:
             cont = cont + 1
             ListaAux2 = a[:c]
             if ListaAux2.count(b):
                 cont = cont + 1
          print(cont)
          if cont % 2 == 0 and cont != 0:
             return b
    return NumerosRepetidos[0]





print(f'\033[32;1m{duplicado(l5)}')
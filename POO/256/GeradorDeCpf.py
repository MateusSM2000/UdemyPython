from random import randint

a = randint(0,9)
b = randint(0,9)
c = randint(0,9)
d = randint(0,9)
e = randint(0,9)
f = randint(0,9)
g = randint(0,9)
h = randint(0,9)
i = randint(0,9)

digitos_e_fatores = [(a, 10), (b, 9), (c, 8), (d, 7), (e, 6), (f, 5), (g, 4), (h, 3), (i, 2)]
soma = 0
for n, m in digitos_e_fatores:
    soma += n * m
if soma % 11 < 2:
    digito_1o = 0
else:
    digito_1o = 11 - soma % 11

digitos_e_fatores = [(a, 11), (b, 10), (c, 9), (d, 8), (e, 7), (f, 6), (g, 5), (h, 4), (i, 3), (digito_1o, 2)]
soma = 0
for n, m in digitos_e_fatores:
    soma += n * m
if soma % 11 < 2:
    digito_2o = 0
else:
    digito_2o = 11 - soma % 11

cpf = f'{a}{b}{c}.{d}{e}{f}.{g}{h}{i}-{digito_1o}{digito_2o}'

print(cpf)
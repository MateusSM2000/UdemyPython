from secrets import SystemRandom
import string as s

random = SystemRandom()  #dessa forma temos uma forma segura de aleatoriedade para criptografias e senhas

print(''.join(random.choices(s.ascii_letters + s.digits + s.punctuation, k=random.randint(8,16))))
print()

lista = [1, 2, 3, 4]
random.shuffle(lista)
print(lista)
print()

nova_lista = random.sample(lista, 3)
print(nova_lista)
print()

nova_lista = random.choices(lista, k=2)  #esse pode repetir o msm valor
print(nova_lista)
print()

nova_lista = random.choice(lista)
print(nova_lista)
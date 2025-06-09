#nao serve para criptografia e senhas pq isso na vdd n é 100% aleatório
import random

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
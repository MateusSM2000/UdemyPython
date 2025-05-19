#usar import só funciona uma vez, se quiser importar dnv tem q usar metodo do importlib
import importlib

for i in range(10):
    print(i)
    importar = __import__('156_m')

print('\n\n\n')


for i in range(10):
    print(i)
    importlib.reload(importar)



import os

print(os.path.expanduser('~'))
NOVA_PASTA = os.path.join(os.path.expanduser('~'), 'Desktop', 'NovaPasta')
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA, exist_ok=True)

#olhar o video da aula pq ele faz cópia de pastas e na aula 287 fala como remove arquivos e pastas e como renomear ou mover pra outro lugar
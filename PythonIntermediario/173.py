import itertools
for n in itertools.count():
    if n > 10:
        break
    print(n)

print('\n\n\n\n')

for n in itertools.count(3):
    if n > 11:
        break
    print(n)

print('\n\n\n\n')

for n in itertools.count(3, 10):
    if n > 100:
        break
    print(n)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dt = pt + (10 - 1) * r
for c in range(pt, dt + r, r):
    print(c, end=' -> ')
print('ACABOU')

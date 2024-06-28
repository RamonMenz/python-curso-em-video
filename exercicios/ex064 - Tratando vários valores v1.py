n = c = t = 0
print('[Digite 999 para parar]')
while n != 999:
    n = int(input('Digite um número: '))
    c += 1
    t += n
print('Você digitou {} números e a soma entre eles foi {}.'.format(c - 1, t - 999))

t = 1
n = int(input('Digite um número para calcular seu fatorial: '))
print('{}! = '.format(n), end='')
while n != 1:
    print(n, 'x', end=' ')
    t *= n
    n -= 1
print('1 = {}'.format(t))

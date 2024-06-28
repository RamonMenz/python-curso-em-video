n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
        print('\033[32m{}\033[m'.format(c), end=' ')
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')
print('\nO número {} é divisível por {} números.'.format(n, cont))
if cont == 2:
    print('E por isso ele \033[32mÉ PRIMO\033[m!')
else:
    print('E por isso ele \033[33mNÃO É PRIMO\033[m!')

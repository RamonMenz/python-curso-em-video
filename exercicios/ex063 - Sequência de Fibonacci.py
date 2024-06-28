print('-=-' * 15)
print('Sequência de Fibonacci')
print('-=-' * 15)
t = int(input('Quantos termos você quer mostrar? '))
c = 0
n1 = 0
n2 = 1
while c != t:
    c += 1
    n3 = n1 + n2
    print('{}'.format(n1), end=' -> ')
    n1 = n2
    n2 = n3
print('ACABOU')

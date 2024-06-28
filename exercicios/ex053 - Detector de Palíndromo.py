f = str(input('Digite uma frase: ')).upper()
fs = f.replace(' ', '')
fi = ''
print('O inverso de {} é '.format(fs), end='')
for c in range(len(fs) - 1, - 1, - 1):
    fi += fs[c]
print(fi + '.')
if fs == fi:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

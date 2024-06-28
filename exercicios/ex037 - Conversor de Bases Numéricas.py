n = int(input('Digite um número inteiro: '))
print('''BASES DE CONVERSÃO:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
b = int(input('Escolha a base de conversão: '))
if b == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif b == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif b == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')

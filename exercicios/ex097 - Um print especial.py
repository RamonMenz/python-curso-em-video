def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


# Programa principal
m = input('Digite uma mensagem: ')
escreva(m)

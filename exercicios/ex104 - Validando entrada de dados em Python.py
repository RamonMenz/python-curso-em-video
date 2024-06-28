def leiaint(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')

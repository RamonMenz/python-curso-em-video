while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-=-' * 13)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-=-' * 13)
print('Tabuada encerrada. Volte sempre!')

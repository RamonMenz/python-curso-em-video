t = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os seguintes valores: {t}')
print(f'Quantidade de vezes que o valor 9 foi digitado: {t.count(9)}')
print('Posição do valor 3: ', end='')
if 3 in t:
    print(f'{t.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado.')
print('Valores pares digitados: ', end='')
cont = 0
for c in t:
    cont += 1
    if c % 2 == 0:
        print(c, end=' ')
if cont == 0:
    print('Não foi digitado nenhum valor par.')
 
dic = {}
lista = []
m = 0
while True:
    print('-' * 25)
    dic['Nome'] = input('Nome: ')
    while True:
        dic['Sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if dic['Sexo'] in 'MF':
            break
        print('Dados inválidos! Tente novamente.')
    dic['Idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    while True:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r in 'SN':
            break
        print('Dados inválidos! Tente novamente.')
    if r == 'N':
        break
print('-=' * 20)
print(f'{len(lista)} pessoas foram cadastradas.')
for c in lista:
    m += c['Idade']
print(f'A média de idade é de {m / len(lista):.2f} anos.')
print(f'Lista das mulheres cadastradas:')
for c in lista:
    if c['Sexo'] == 'F':
        print(f'- {c["Nome"]}')
print('Lista das pessoas que estão acima da média de idade:')
print('-' * 25)
for c in lista:
    if c['Idade'] > m / len(lista):
        for v, k in c.items():
            print(f'- {v}: {k}')
        print('-' * 25)

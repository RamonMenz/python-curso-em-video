lista = []
nome = []
notas = []
while True:
    n = input('Nome: ')
    nome.append(n)
    for c in range(1, 3):
        notas.append(float(input(f'Nota {c}: ')))
    nome.append(notas[:])
    lista.append(nome[:])
    nome.clear()
    notas.clear()
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        print('=-' * 15)
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>15}')
print('_' * 30)
for d in lista:
    print(f'{lista.index(d) + 1:<4}{d[0]:<10}{sum(d[1]) / 2:>14.2f}')
print('=-' * 15)
while True:
    print('-' * 50)
    r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if r == 999:
        break
    else:
        print(f'Notas do(a) {lista[r - 1][0]}: {lista[r - 1][1]}')
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')

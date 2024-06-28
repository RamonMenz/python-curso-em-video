s = 0
while s != 'M' and s != 'F':
    s = input('Informe seu sexo: [M/F] ').strip().upper()[0]
    if s in 'MF':
        print('Sexo {} registrado com sucesso.'.format(s))
    else:
        print('Dados inválidos. Por favor, ', end='')

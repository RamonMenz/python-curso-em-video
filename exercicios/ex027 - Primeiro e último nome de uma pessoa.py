n = str(input('\033[34mDigite seu nome completo:\033[m ')).strip().split()
print('Seu primeiro nome é \033[4;33m{}\033[m.'.format(n[0]))
print('Seu último nome é \033[4;33m{}\033[m.'.format(n[len(n)-1]))

c = input('\033[34mDigite o nome da sua cidade: \033[m')
print('O nome da sua cidade começa com \033[4;33m"Santo"\033[m: {}'.format('santo' in c.lower().split()[0]))

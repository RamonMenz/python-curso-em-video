n = int(input('\033[34mMe diga um número qualquer:\033[m '))
if n % 2 == 0:
    print('O número {} é \033[4;36mPAR\033[m.'.format(n))
else:
    print('O número {} é \033[4;36mÍMPAR\033[m.'.format(n))

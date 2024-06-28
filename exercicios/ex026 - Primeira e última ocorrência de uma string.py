f = str(input('\033[34mDigite uma frase:\033[m ')).strip().lower()
print('A \033[4;33mletra A\033[m apareceu {} vezes na frase.'.format(f.count('a')))
print('A primeira \033[4;33mletra A\033[m apareceu na posição {}.'.format(f.find('a') + 1))
print('A última \033[4;33mletra A\033[m apareceu na posição {}.'.format(f.rfind('a') + 1))

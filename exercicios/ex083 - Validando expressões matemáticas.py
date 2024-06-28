lista = []
e = input('Digite uma expressão matemática: ')
for c in e:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(e) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

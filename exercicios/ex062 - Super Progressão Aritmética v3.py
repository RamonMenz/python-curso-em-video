pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = c = cont = 0
x = 10
while x != 0:
    t += x
    while c != t:
        print(pt, end=' -> ')
        c += 1
        pt += r
        cont += 1
    x = int(input('PAUSA\nQuantos termos você quer mostrar a mais? '))
print('Progreção finalizada com {} termos mostrados.'.format(cont))

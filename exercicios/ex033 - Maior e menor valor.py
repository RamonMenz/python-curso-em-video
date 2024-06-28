a = int(input('\033[4;34mPrimeiro valor:\033[m '))
b = int(input('\033[4;34mSegundo valor:\033[m '))
c = int(input('\033[4;34mTerceiro valor:\033[m '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O \033[35mmenor\033[m valor digitado foi \033[35m{}\033[m.'.format(menor))
print('O \033[35mmaior\033[m valor digitado foi \033[35m{}\033[m.'.format(maior))

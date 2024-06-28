from random import randint
n = t = 0
num = randint(0, 10)
print('\033[33m-=-\033[m' * 18)
print('\033[35mPensei em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 18)
while n != num:
    n = int(input('Em que número eu pensei? '))
    t += 1
    if n == num:
        if t == 0:
            print('\033[32mPARABÉNS! Você acertou de primeira!\033[m')
        else:
            print('\033[32mPARABÉNS! Você acertou com {} tentativas!\033[m'.format(t))
    elif n < num:
        print('\033[31mMais... Tente mais uma vez.\033[m')
    else:
        print('\033[31mMenos... Tente mais uma vez.\033[m')

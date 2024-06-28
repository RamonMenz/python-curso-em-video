from random import randint
from time import sleep
num = randint(0, 5)
print('\033[33m-=-\033[m' * 18)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 18)
n = int(input('Em que número eu pensei? '))
print('\033[34mPROCESSANDO...\033[m')
sleep(3)
if n == num:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}.\033[m'.format(num, n))

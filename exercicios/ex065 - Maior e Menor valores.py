n = q = r = s = 0
maior = menor = 0
while r != "N":
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('Você digitou {} números e a média foi {:.2f}.'.format(q, s / q))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

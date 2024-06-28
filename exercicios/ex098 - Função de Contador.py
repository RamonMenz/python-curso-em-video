def contador(ini, fim, pas):
    from time import sleep
    print('=-' * 20)
    if pas < 0:
        pas *= -1
    elif pas == 0:
        pas = 1
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}:')
    sleep(1.5)
    if ini < fim:
        while ini <= fim:
            print(ini, end=' ')
            ini += pas
            sleep(0.25)
    elif ini > fim:
        while ini >= fim:
            print(ini, end=' ')
            ini -= pas
            sleep(0.25)
    print('FIM!')
    sleep(1)


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20, '\nAgora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

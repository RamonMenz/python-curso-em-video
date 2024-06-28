t = ('aprender', 'programar', 'linguagem', 'python',
     'curso', 'gratuito', 'estudar', 'praticar',
     'trabalhar', 'mercado', 'programador', 'futuro')
for p in t:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for d in range(0, len(p)):
        if p[d] in 'aeiou':
            print(p[d], end=' ')

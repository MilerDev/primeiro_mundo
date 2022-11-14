print('olar ')
c = input('como vai?')
if c == 'bem':
    print('que otimo!')
    n = input('voce que somar dois numeros ?[s/n]')
    if n == 's':
        n1 = int(input('legal! então digite um numero :'))
        n2 = int(input('digite outro numero :'))
        c1 = n1 + n2
        print('a soma entre {} e {} é {} , um bom dia !'.format(n1, n2, c1))
elif c == 'nao ben':
    print('espero que seu dia seja bom !')

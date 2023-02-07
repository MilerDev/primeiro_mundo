# faze 10

n1 = float(input('digite a primeira nota :'))
n2 = float(input('digite a segunda nota:'))
m = (n1 + n2) / 2
print('a sua media foi {:.1f}'.format(m))
if m >= 6:
    print('parabens!')
else:
    print('estude mais !')

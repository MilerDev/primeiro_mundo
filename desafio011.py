# desafio 011 faça uma programa que leia a largura e altura de uma parede em metros , calcule a sua area e a
# quantidade de tinda necessaria para pintar-la ,sabendo que cada litro de tinta pinta uma area de 2m.
l = float(input('qual a largura da parede?'))
a = float(input('qual altura da parede?'))
area = l * a
print('sua parede tem a dimensao de {}x{} e sua area é de {}m'.format(l, a, area))
t = area /2
print('para pintar essa parede ,voce precisara de {}l de tinta'.format(t))
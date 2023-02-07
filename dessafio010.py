# crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# considere Uss1.00=Rs3.27
r = float(input('quandos dinheiro voce tem na cadeira? r$'))
d = r/3.27
print('com R${:.2f}  voce pode comprar uss{:.2f}'.format(r, d))
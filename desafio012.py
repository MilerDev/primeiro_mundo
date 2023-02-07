# desafio 012 - faça um algoritimo que leia o preço de um produto e moste seu novo preço, com 5% de desconto
p = float(input('qual o valor do produto? R$'))
n = p - (p * 5/100)
print('o produto que custava R${:.2f} , na promoçao com desconto de 5% vai custar R${:.2f} '.format(p, n))



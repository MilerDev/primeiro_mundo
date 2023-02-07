# escreva um programa que perguntte a quantidade de Km percorridas por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado .
# calcule o preço a pagar ,sabendo que o carro custa R$60 por dia e R$por Km rodado.
d = float(input('quandos dias alugados?'))
km = float(input('quantos Km rodados?'))
p = (d * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(p))




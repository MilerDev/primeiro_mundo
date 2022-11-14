# desenvolva um programa que pergunte a distancia de uma viagem em
# Km.calcule o preço da passagem.cobrando R$0,50 por Km
# para viagens de ate 200Km e R$0,45 para viagens mais longas.
d = float(input('qual é a distancia da sua viagem?'))
print('voce estar a começar uma viagemde {}Km'.format(d))
'''if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45'''
preço = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 8km/h, mostre uma mensagem dizendo que ele
# foi multado.
# a muçta vai custar r$7,00 por cada km acima do limite.
v = float(input('qual a velocidade do seu carro?'))
if v > 80:
    print('MULtaDO! voce exedeu o limite permitido que é de 80km/h ')
    m = (v - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(m))
print('tenha um bom dia! DIRIJA com segurança!')
# escreva um programa que pergunte o salario de um funcionario é calcule o valo
# do aumento.para salarios superiores a R$1250,00 , calcule um aumento de 10%.
# para os inferiore ou iguais , o aumento é de 15%.
salario = float(input('qual o seu salario atual?'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
    print('seu salario deve 10% de aumento , agora é {}'.format(aumento))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
    print('seu salario deve 15% de aumento, agora é {:.2f}'.format(aumento))
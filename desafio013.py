# faça um algoritimo que leia o salario de um funcionario e motre seu novo salario com 15% de aumento
s = float(input('qual o salario do funcionario? R$'))
n = s + (s*15/100)
print('um funcionario que ganhava R${:.2f} , com 15% de almento ,passa a receber R${:.2f}'.format(s, n))
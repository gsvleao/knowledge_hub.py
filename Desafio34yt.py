"""
Exercício Python 034:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
print('=-' * 10, 'Desafio 34', '-=' * 10)

salario = float(input('Qual o atual salário do funcionário? R$'))

if salario > 1.250:
    print('Será atribuído uma aumento de 10% ao valor de R${:.3f}. O salário atualizado será de {:.3f}.'.format(salario, salario + (salario * 10 / 100)))
else:
    print('Será atribuído uma aumento de 15% ao valor de R${:.3f}. O salário atualizado será de {:.3f}.'.format(salario, salario + (salario * 15 / 100)))
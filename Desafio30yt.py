"""
Exercício Python 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

print('=-' * 12, 'Desafio 30', '-=' * 12)

numero = int(input('Me diga um número: '))
result = numero % 2 # o resto da divisão de um número ímpar será sempre 1, de um par, sempre 0.

if result == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))

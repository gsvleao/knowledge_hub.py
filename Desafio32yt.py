"""
Exercício Python 032:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
from datetime import date

print('=-' * 12, 'Desafio 32', '-=' * 12)

ano = int(input('Que ano deseja analisar? Digite 0 (zero) para analisar o ano atual: '))

# Obs: se um ano é divisível por 4, então ele é bissexto (exceto anos múltiplos de 100 que não são múltiplos de 400).
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto.'.format(ano))
else:
    print('{} não é um ano Bissexto.'.format(ano))

"""
Exercício Python 031:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

print('=-' * 12, 'Desafio 31', '-=' * 12)

dist = float(input('Qual é a distância do seu destino de viagem em Km? '))

print('Você fará uma viagem de {:.0f}Km?'.format(dist))

if dist <= 200:
    print('O preço da sua passagem será R${:.2f}'.format(dist * 0.50))
else:
    print('O preço da sua passagem será R${:.2f}'.format(dist * 0.45))

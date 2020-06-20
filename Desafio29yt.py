"""
Exercício Python 029:
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
print('=-' * 12, 'Desafio 29', '-=' * 12)

velo = float(input('Qual a velocidade do carro em Km/h? '))
multa = (velo - 80) *7

if velo <= 80:
    print('Tenha um bom dia! Dirija em segurança.')
else:
    print('Você está acima do limite de velocidade permitido. Você foi multado em R${:.2f}.'.format(velo))


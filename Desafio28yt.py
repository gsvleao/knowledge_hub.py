"""
Exercício Python 028:
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
print('=-' * 12, 'Desafio 28', '-=' * 12)

import random
import time
num = random.randint(0, 3)

print('=_' * 31)
print('Vou pensar em um número entre 0 e 5 e você vai tenta advinhar.')
print('=_' * 31)

ent = int(input('Em qual número eu pensei: '))
print('Consultando os Oráculos Matemáticos Transcendentais...')
time.sleep(3)
print('Hackeando sua mente involuída...')
time.sleep(3)

if ent == num:
    print('Parabéns! Você advinhou, seu Bruxão!')
else:
    print('Not today, Jesus! Eu pensei em {}.'.format(num))
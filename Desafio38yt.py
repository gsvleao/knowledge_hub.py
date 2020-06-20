"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
Mostre na tela uma mensagem indicando qual o maior valor.
"""
print('=-=' * 10, 'Desafio 38', '=-=' * 10)

primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))

if primeiro_num > segundo_num:
    print('O primeiro número é MAIOR que o segundo.')
elif segundo_num > primeiro_num:
    print('O segundo número é MAIOR que o primeiro.')
else:
    print('Esses números são IGUAIS.')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo.
# E também todas as informações sobre ele.

from os import system

system('clear')

usuario = input("Digite algo e abaixo vai ter o seu tipo primito: ")




if usuario.isdigit() == True:
    print(f"\n{usuario} é um número inteiro!")
elif isinstance(usuario, str):
    print(f'\n"{usuario}" -> É uma string ou algum variate como float, boleano, etc...')
    print(f'O tipo primito é {type(usuario)}')
    print(f'A string só tem espaço: {usuario.isspace()}')
    print(f'É um valor númerico inteiro: {usuario.isdigit()}')
    print(f'')

else:
    print('\nValor não identificado, tente novamente :)')

# Crie um algoritmo que leia um número e mostre o seguinte
# Seu dobro, triplo e raiz quadrada

from os import system

system('clear')

num = float(input('Digite um número: '))

print(f'\nO dobro de {num} é {num*2}\nO triplo de {num} é {num*3}\nE sua raiz quadrada é {pow(num, 0.5)}')
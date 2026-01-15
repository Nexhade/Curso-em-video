#Faça um programa que leia um número inteiro
#Faça um tabuada desse número

from os import system

system('clear')

print("Tabuada")

num = int(input('\nDigite o número para gerar sua tabuada: '))
print('\n')
base = 0
while base != 11:
    print(f'{num}X{base} = {num*base}')
    base +=1
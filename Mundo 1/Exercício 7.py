#Deselvolva um programa que leia duas notas de um aluno
#Calcule e mostre a sua média

from os import system

system('clear')

print('Sitema para calucar a média de um aluno')

nota1 = float(input('\nDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'\nA média das duas notas é {(nota1+nota2)//2}')
#Crie um programa que leia dois números e mostre a soma entre eles

from os import system

system("clear")

print('Soma entre dois números\n')

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

system("clear")

print(f'{num1} + {num2} = {num1+num2}')
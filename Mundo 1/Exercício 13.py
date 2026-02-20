#Faça um algoritmo que leia o salário de um funcionário
#Após isso mesmo o valor reajustado com um aumento de 15%

from os import system

system('clear')

salario = float(input('Digite o seu salário: '))

print(f'Seu salário com reajuste de 15% é R${(salario + ((15/100)*salario))}')
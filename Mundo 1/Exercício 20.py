#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada

from os import system
import random

system('clear')

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

system('clear')

lista = [aluno1, aluno2, aluno3, aluno4]

print(f'A ordem para chamar os aluno para apresentar o trabalho é {random.choices(lista, k=4)}') #O K=4 é para definir quantos itens aleatórios devem aparecer


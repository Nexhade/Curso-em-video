#Um professor que sortear um dos seus quatros alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from os import system
import random

system('clear')

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

system('clear')

print(f'O aluno escolhido foi: {random.choices(lista)}')


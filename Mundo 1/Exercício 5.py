# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

from os import system

system('clear')

print('Digite um número inteiro que mosto seu sucesso e antecessor!\n')

num = int(input("Digite um número inteiro: "))

system('clear')

print(f'{num} foi o número digitado, {num + 1} é o seu sucessor e {num -1} é seu antecessor!')

#Escreva um programa que leia um valor em metros
#Retorne o valor convertido em centímetros e milímetros

from os import system

system('clear')

print('Sistem de conversão Metros em Centímetros / Milímetros')

metros = float(input('\nDigite o valor em metros: '))

print(f'\n{metros} metro(s) em centimetros é {metros * 100}\n{metros} metro(s) em milímeros é {metros * 1000}')

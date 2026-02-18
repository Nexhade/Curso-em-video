#Faça um programa que leia o preço de um produto
#Após isso, mostre seu preço com 5% de desconto

from os import system

system('clear')

preco = float(input('Digite o preço do seu produto: '))

print(f'\nO valor do seu produto com 5% de desconto é R${(preco - ((5/100)*preco))}')
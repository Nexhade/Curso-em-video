# Crie um programa que leia quanto dinheiro uma pessoa tem
# Após isso conversa em dolar e mostre o resultado

from os import system

system('clear')

dolar = 4.12

real = float(input("Quanto tem a sua carteira: "))

print(f"Convertendo os seus R${real} para dolar temos o total arredondado de USS{real // dolar}")
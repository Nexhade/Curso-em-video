#Escreva um progrma que converta temperatura
#Usuario vai digitar em graus celsius e converta para graus farenheit

from os import system

system('clear')

temp = float(input("Digite a temperatura em Graus Celsius para a conversão em Fahrenheit: "))

print(f'\nO resultado da conversão de {temp} Graus Celsius da {(temp*1.8)+32} Graus Fahrenheit')

#Faça um programa que leia o comprimeiro do cateto oposto e do cateto adjacente de um triangulo retângulo
#Calcule e mostre o comprimeiro da hipotenusa

from os import system

system('clear')

c_oposto = float(input('Digite o valor do cateto oposto: '))
c_adjacente = float(input('Digite o valor do cateto adjacente: '))

print(f"\nO valor da sua hipotenusa é {pow((c_oposto**2 + c_adjacente**2), 0.5):.2f}")
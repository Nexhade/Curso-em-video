#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from os import system
from math import cos, sin, tan

system("clear")

angulo = float(input("Digite o valor do seu ângulo: "))

system('clear')

print(f'''\nPara o ângulo {angulo}, temos:\n
      Tangente: {tan(angulo):.2f}
      Seno: {sin(angulo):.2f}
      Cosseno: {cos(angulo):.2f}''')

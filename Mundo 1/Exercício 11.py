#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule sua área e quantidade de tinta necessária para pinta-lá
#Sabe-se que cada litro de tinta pinta uma área de 2 metros quadrados

from os import system

system('clear')

largura = float(input("Digite a largura da sua parede em metros: "))
altura = float(input("Digite a altura da sua parede: "))
metragem = altura*largura

system('clear')

if (metragem % 2 == 0):
    print(f'Você de exatamente {metragem//2}, litros de tinta')
else:
    print(f'Você precisa de {metragem/2} litros de tinta, como é um valor quebrado recomendo pegar', {(metragem/2)+1})

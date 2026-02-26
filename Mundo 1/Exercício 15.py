#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

from os import system

system("clear")

carro_alu = int(input('Ficou com o carro alugado por quantos dias: '))
km_per = float(input('Digite a quantidade de km percorrido: '))

#total = (carro_alu*60)+(km_per*0,15)

print(f'VOcê alugou o carro por {carro_alu} dias, o valor a pagar é R${(carro_alu*60)+(km_per*0.15)}')
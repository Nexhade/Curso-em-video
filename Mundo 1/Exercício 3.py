"""Crie um programa que leia dois números e mostre a soma entre eles."""

from os import system

system("clear")

print("--- Soma de dois números ---\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\nA soma dos dois número é igual a {num1 + num2}")
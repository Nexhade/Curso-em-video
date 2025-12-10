"""Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas"""

from os import system

nome = input("Qual seu nome?: ")

system("clear")

print(f"Seja bem vindo", nome,":)")
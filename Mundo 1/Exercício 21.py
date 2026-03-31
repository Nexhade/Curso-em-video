#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

from os import system
import pygame

system('clear')

print('Teste de audio padrão')

pygame.mixer.init()
pygame.mixer.music.load("audio.mp3")
pygame.mixer.music.play()

input("\nPrecione 'Enter' tecla para sair...")

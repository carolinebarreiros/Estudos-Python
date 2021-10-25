#Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
input('Agora eu escuto?')
pygame.event.wait()
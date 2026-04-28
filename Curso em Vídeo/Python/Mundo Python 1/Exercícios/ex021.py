import pygame
pygame.init()
pygame.mixer.music.load(r'C:\Users\guisi\OneDrive\Documentos\Naruto Shippuden Abertura 3 Completa em Português - Blue Bird (PT-BR).mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
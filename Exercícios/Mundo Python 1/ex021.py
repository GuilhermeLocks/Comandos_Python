import pygame
pygame.init()
pygame.mixer.music.load(r'C:\Users\guisi\Downloads\13 Mac Apps I (Almost) Cant Live Without.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10) 
import pygame
import emoji
print(emoji.emojize('\033[7;34m:musical_notes::musical_notes:Aproveite a música!:musical_notes::musical_notes:\033[m'))
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()
pygame.event.wait()

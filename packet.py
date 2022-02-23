"""
EasyGame

Description:
"""
import pygame, sys
pygame.init()

run = True

surface = pygame.display.set_mode((800, 800))
    
def Button(buttonX, buttonY, width, height, color, text):
        
    pygame.draw.rect(surface, color, pygame.Rect(buttonX, buttonY, width, height))
    pygame.display.flip()

def Switch(buttonX, buttonY, width, height, color, text):
    
    obj = pygame.Rect(buttonX, buttonY, width, height)
    
    pygame.draw.rect(surface, color, obj)
    pygame.display.flip()
    
    isSwitched = False
    
    while True:
        
        mouse = pygame.mouse.get_pos()
        btnObj = (obj.width, obj.height)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                if mouse == btnObj:
                    
                    isSwitched = not isSwitched
                    print(isSwitched)
    
def AudioSource(fileName, loop, isPlaying):
    
    soundFile = pygame.mixer.Sound(fileName + ".mp3")
    
    if isPlaying:
        
        if loop:
        
            soundFile.play(-1)
        
        else:
            
            soundFile.play()

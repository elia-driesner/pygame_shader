import pygame, sys

'''
This file is to test the performance with and without moderngl

Without ModernGL 120 FPS (This file)
With ModernGL 670 FPS (shaders.py)
'''

display = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
img = pygame.image.load('img.png')


while True:
    display.fill((0, 0, 0))
    display.blit(img, pygame.mouse.get_pos())
    print(clock.get_fps())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.flip()
    clock.tick(1000)
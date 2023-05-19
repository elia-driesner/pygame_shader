import pygame, sys

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
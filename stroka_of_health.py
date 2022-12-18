import pygame

WIDTH = 1200
HEIGHT = 700
FPS = 200
BLACK = (0, 0, 0)

pygame.init()
pygame.Surface((100, 80))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Физтех.life")
clock = pygame.time.Clock()

image = pygame.image.load("heart.png")
image = pygame.transform.scale(image, (50, 35))
image.set_colorkey((255, 255, 255))

running = True
while running:
    clock.tick(FPS)

    string =  pygame.Rect(0 , 0, WIDTH, 0).inflate(1200, 100)
    screen.fill((128, 128, 128))
    
    pygame.draw.rect(screen, BLACK, string)
    
    screen.blit(image, (20, 10 ))

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
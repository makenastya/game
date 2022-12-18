import pygame

WIDTH = 1200
HEIGHT = 700
PANTONE_148 = (244, 209,153)
PANTONE_201 = (161, 42, 61)
FPS = 200


pygame.init()
pygame.Surface((100, 80))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Физтех.life")
clock = pygame.time.Clock()

arial_font = pygame.font.SysFont("Arial Black", 40)
text = arial_font.render("Поздравляем! Ты победил", True, PANTONE_201 )
image = pygame.image.load("win.jpg")
image = pygame.transform.scale(image, (600, 500))

running = True
while running:

    screen.fill(PANTONE_148)
    screen.blit(text, ((WIDTH / 2) - 300, 30))
    screen.blit(image, (WIDTH / 4 , HEIGHT / 4 - 30 ))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
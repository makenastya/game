import pygame

def game_over():
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
    text = arial_font.render("GAME OVER", True, PANTONE_201 )
    image = pygame.image.load("рыба.jpg")

    running = True
    while running:

        screen.fill(PANTONE_148)
        screen.blit(text, ((WIDTH / 2) - 150, 30))
        screen.blit(image, (WIDTH / 4 + 30, HEIGHT / 4 - 30 ))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
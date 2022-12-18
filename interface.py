import pygame

WIDTH = 1200
HEIGHT = 700
FPS = 200

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PANTONE_148 = (244, 209,153)
PANTONE_257 = (43, 116, 183)
main_button_color = (0,128,94)
PANTONE_351 = (196, 225, 222)
second_button_color = (124,187,90)


pygame.init()
pygame.Surface((100, 80))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Физтех.life")
clock = pygame.time.Clock()



arial_font = pygame.font.SysFont("Arial Black", 40)
butten_font = pygame.font.SysFont("Arial", 22)
level_choice_font = pygame.font.SysFont("Arial", 30)

text = arial_font.render("Welcome to MIPT", True, PANTONE_257 )
level_choice_text = level_choice_font.render("Выберите уровень сложности", True, BLACK)
butten_1_text = butten_font.render("Вы на БТ ", True, PANTONE_351 )
butten_2_text = butten_font.render("Вы все еще БТ, но взяли себе вычматы", True, PANTONE_351 )
butten_3_text = butten_font.render("Вы ПМФ, соболезнуем", True, PANTONE_351)

running = True
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    button_1 =  pygame.Rect(WIDTH / 2 , HEIGHT / 2 - 80, 0, 0).inflate(500, 40)
    button_2 =  pygame.Rect(WIDTH / 2 , HEIGHT / 2 + 20, 0, 0).inflate(500, 40)
    button_3 =  pygame.Rect(WIDTH / 2 , HEIGHT / 2 + 120, 0, 0).inflate(500, 40)
    collide_1 = button_1.collidepoint(mouse_pos) 
    collide_2 = button_2.collidepoint(mouse_pos)
    collide_3 = button_3.collidepoint(mouse_pos) 
    color_1 = second_button_color if collide_1 else main_button_color 
    color_2 = second_button_color if collide_2 else main_button_color
    color_3 = second_button_color if collide_3 else main_button_color

    #прорисовка меню
    screen.fill(PANTONE_148)
    pygame.draw.rect(screen, color_1, button_1)
    pygame.draw.rect(screen, color_2, button_2)
    pygame.draw.rect(screen, color_3, button_3)
    screen.blit(butten_1_text, ((WIDTH / 2) - 40, HEIGHT / 2 - 95 ))
    screen.blit(butten_2_text, ((WIDTH / 2) - 160, HEIGHT / 2 + 5))
    screen.blit(butten_3_text, ((WIDTH / 2) - 100, HEIGHT / 2 + 105))
    screen.blit(text, ((WIDTH / 2) - 200, 30))
    screen.blit(level_choice_text, (WIDTH / 2 - 180, 150) )
    #выбор уровня в меню, либо выход




    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (WIDTH / 2 - 250) <= mouse_pos[0] <= (WIDTH / 2 + 250) and (HEIGHT / 2 -100) <= mouse_pos[1] <= (HEIGHT / 2- 60):
                    #running = False
                    #запуск основной программы
                level = 1
            if (WIDTH / 2 - 250) <= mouse_pos[0] <= (WIDTH / 2 + 250) and (HEIGHT / 2 ) <= mouse_pos[1] <= (HEIGHT / 2 + 40):
                level = 2
            if (WIDTH / 2 - 250) <= mouse_pos[0] <= (WIDTH / 2 + 250) and (HEIGHT / 2 +100) <= mouse_pos[1] <= (HEIGHT / 2 + 140):
                level = 3

    

    
pygame.quit()


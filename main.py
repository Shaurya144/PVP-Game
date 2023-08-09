import pygame

pygame.init()

# create screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 663
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PVP Game")

# setting background
bg_image = pygame.image.load("assets/firstbackground.jpg").convert_alpha()

def draw_bg():
    screen.blit(bg_image, (0, 0))

# game loop
run = True
while run:

    # draw background
    draw_bg()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# exit game
pygame.quit()
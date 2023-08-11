import pygame

pygame.init()

# create screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 663
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PVP Game")

# setting up images
bg_image = pygame.image.load("assets/firstbackground.jpg").convert_alpha()
bg_island_biulding = pygame.image.load("assets/floatingislandcopy.png").convert_alpha()
bg_island = pygame.image.load("assets/bgisland.png").convert_alpha()
bg_island = pygame.transform.scale(bg_island, (450, 225))
bg_island_biulding = pygame.transform.scale(bg_island_biulding, (450, 225))



def draw_bg():
    screen.blit(bg_image, (0, 0))

def draw_island():
    screen.blit(bg_island, (287, 125))
    
def draw_building():
    screen.blit(bg_island_biulding, (300, 350))

# game loop
run = True
while run:

    # draw everything
    draw_bg()
    draw_building()
    draw_island()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

# exit game
pygame.quit()

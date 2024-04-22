import pygame as pg

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initialization
pg.init()

# Window
width = 1000
height = 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Game")

# Background color
screen.fill(black)

# Shape
# pg.draw.rect(screen, red, (100, 100, 120, 120))

# Images
hp_image = pg.image.load("img/icon.png")
hp_rect = hp_image.get_rect()
hp_rect.center = (width/2, height/2)

# Mainloop
lets_continue = True

while lets_continue:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            lets_continue = False

    # Bliting
    screen.blit(hp_image, hp_rect)

    # Screen update
    pg.display.update()

# End
pg.quit()

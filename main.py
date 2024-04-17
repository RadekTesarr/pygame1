import pygame as pg
import pygame.display

# Colors def
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Initialization
pg.init()

# Display window
width = 600
height = 300
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Harry Potter Game")

screen.fill(red)

# Mainloop
lets_continue = True

while lets_continue:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            lets_continue = False

    # Refresh
    pygame.display.update()

# End of pygame
pg.quit()

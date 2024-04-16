import pygame as pg

# Initialization
pg.init()

# Display window
width = 600
height = 300
screen = pg.display.set_mode((width, height))

# Mainloop
lets_continue = True

while lets_continue:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            lets_continue = False

# End of pygame
pg.quit()

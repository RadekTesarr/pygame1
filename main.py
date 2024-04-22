import pygame as pg

# Init
pg.init()

# Window
width = 600
height = 300
screen = pg.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# System fonts
# fonts = pg.font.get_fonts()
# for i in fonts:
#     print(i)      freesans

# Font set
sys_font = pg.font.SysFont("arial", 32)

# Font & text
sys_text = sys_font.render("Harry Potter", True, white, red)
sys_text_rect = sys_text.get_rect()
sys_text_rect.center = (width//2, height//2)

# Mainloop
lets_continue = True
while lets_continue:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            lets_continue = False

    # Text blit
    screen.blit(sys_text, sys_text_rect)

    # Screen update
    pg.display.update()

# End
pg.quit()
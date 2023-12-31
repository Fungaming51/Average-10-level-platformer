import pygame as pg

window = pg.display.set_mode((300, 300))

pg.display.set_caption("Average 10 level platformer")

pg.display.flip()
running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

            pg.quit()

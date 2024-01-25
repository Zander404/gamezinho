import pygame as pg

WIDTH, HEIGHT = 900, 500
FPS = 60


test_surface = pg.Surface((100,200))
test_surface.fill("white")

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Gamer")
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.blit(test_surface, (0,0))
    
    pg.display.update()
    clock.tick(FPS)
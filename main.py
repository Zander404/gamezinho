import pygame as pg 
from sys import exit 

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Runner")
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


        ## Pintar o Fundo de Preto
        screen.fill('black')
        

        
    
    pg.display.update()
    clock.tick(60)
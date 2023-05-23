import Class
import pygame as pg
pg.init()

win_x, win_y = 800, 680
screen = pg.display.set_mode((win_x, win_y))
FONT = pg.font.Font(None, 32)
error = True

scene1 = Class.Simulation(180,290)
scene2 = Class.Calculator(65, 400)

while True:
    screen.fill((255,255,255))
    scene1.drawProjectile(5, screen)
    scene2.draw(screen)

    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get():
        scene2.updateEvent(event)
        if event.type == pg.QUIT: 
            pg.quit()
            exit() 
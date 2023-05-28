import Class
import pygame as pg
pg.init()

win_x, win_y = 800, 680
screen = pg.display.set_mode((win_x, win_y))
FONT = pg.font.Font(None, 32)
error = True

img = ['Xtarget_2\\2.png', 'Xtarget_2\\4.png', 'Xtarget_2\\6.png', 'Xtarget_2\\7.png']
scene1 = Class.Simulation(65, 50)
scene2 = Class.Calculator(65, 430)
scene3 = Class.Manual(img,0,0)
main = Class.MainWindow(scene1,scene2,scene3)

while True:
    screen.fill((255,255,255))
    main.main(5,screen)
    # scene3.draw(screen)

    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get():
        main.mainUpdateEvent(event)
        # scene3.updateEvent(event)
        if event.type == pg.QUIT: 
            pg.quit()
            exit() 
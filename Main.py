import Class
import pygame as pg
pg.init()

win_x, win_y = 800, 680
screen = pg.display.set_mode((win_x, win_y))
FONT = pg.font.Font(None, 32)
inactiveColor = (100,100,100)
activeColor = (0,0,0)
error = True

scene1 = Class.Simulation(180,290,230,5.18)
text6 = Class.TextBox(75, 30, 'Simulation', fontSize = 48)
text_boxes = [text6]
button = Class.Button(190, 565, 'Calculate')
scene2 = Class.Calculator(65, 400)

while True:
    screen.fill((255,255,255))
    scene1.drawProjectile(5,screen)
    if not error:
        scene1.status = 1
    scene2.draw(screen)
    button.draw(screen)

    for text in text_boxes:
        text.draw(screen)

    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get():
        if button.isMousePress(event):
            if scene2.targetX.text != '' and scene2.targetY.text != '':
                if float(scene2.targetX.text)>=0 and float(scene2.targetX.text)<=80 and float(scene2.targetY.text)>=0 and float(scene2.targetY.text)<=30:
                    u = scene2.calculate()
                    scene1.changeDistance(float(scene2.targetY.text))
                    scene1.changeVelocity(u)
                    scene1.status = True
                    button.status = True
                    error = False
                    if text8 in text_boxes:
                        text_boxes.remove(text8)
                else:
                    error = True
                    if text8 not in text_boxes:
                        text_boxes.append(text8)
                if text5 in text_boxes:
                    text_boxes.remove(text5)
            else:
                error = True
                if text8 in text_boxes:
                    text_boxes.remove(text8)
                if text5 not in text_boxes:
                    text_boxes.append(text5)
        for box in scene2.inputBoxes:
            box.handleEvent(event)
            box.numberCheck()
        if event.type == pg.QUIT: 
            pg.quit()
            exit() 
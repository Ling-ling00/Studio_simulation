import Class
import math
import pygame as pg
pg.init()

win_x, win_y = 800, 680
screen = pg.display.set_mode((win_x, win_y))
FONT = pg.font.Font(None, 32)
inactiveColor = (100,100,100)
activeColor = (0,0,0)

scene1 = Class.Simulation(150,300,230,5.18)
text1 = Class.TextBox(75, 430, 'Xtarget =                           cm.')
text2 = Class.TextBox(75, 480, 'Ytarget =                           cm.')
text3 = Class.TextBox(425, 430, 'Xrobot  =  ___  cm.')
text4 = Class.TextBox(425, 480, 'Voltage =  ___  V.')
text5 = Class.TextBox(75, 580, 'Please enter number!!')
text_boxes = [text1, text2, text3, text4]
input_box1 = Class.InputBox(175, 425, 150, 32)
input_box2 = Class.InputBox(175, 475, 150, 32)
input_boxes = [input_box1, input_box2]
button = Class.Button(190, 525, 'Calculate')
scene2 = Class.Calculator(65,400,input_box1,input_box2,text4,text3)

while True:
    screen.fill((255,255,255))
    scene1.drawRect(screen)
    scene1.drawProjectile(5,screen)
    scene1.drawField(screen)
    scene2.drawRect(screen)
    button.draw(screen)

    for text in text_boxes:
        text.draw(screen)
    for box in input_boxes:
        box.draw(screen)

    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get():
        if button.isMousePress(event):
            if input_box1.text != '' and input_box2.text != '':
                u = scene2.calculate()
                scene1.changeDistance(float(input_box2.text))
                scene1.changeVelocity(u)
                scene1.status = True
                button.status = True
                if text5 in text_boxes:
                    text_boxes.remove(text5)
            else:
                if text5 not in text_boxes:
                    text_boxes.append(text5)
        for box in input_boxes:
            box.handleEvent(event)
            box.numberCheck()
        if event.type == pg.QUIT: 
            pg.quit()
            exit() 
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
text1 = Class.TextBox(75, 470, 'Xtarget =                           cm.')
text2 = Class.TextBox(75, 520, 'Ytarget =                           cm.')
text3 = Class.TextBox(425, 470, 'Xrobot  =  ___  cm.')
text4 = Class.TextBox(425, 520, 'Voltage =  ___  V.')
text5 = Class.TextBox(225, 200, 'Please enter number!!', (255,0,0), 48)
text6 = Class.TextBox(75, 30, 'Simulation', fontSize = 48)
text7 = Class.TextBox(75, 420, 'Calculator',fontSize = 48)
text8 = Class.TextBox(225, 200, 'Number not in range!!', (255,0,0), 48)
text9 = Class.TextBox(75, 500, 'Please enter number between 0-10', (100,100,100), 18)
text10 = Class.TextBox(75, 550, 'Please enter number between 0-10', (100,100,100), 18)
text_boxes = [text1, text2, text3, text4, text6, text7, text9, text10]
input_box1 = Class.InputBox(175, 465, 150, 32)
input_box2 = Class.InputBox(175, 515, 150, 32)
input_boxes = [input_box1, input_box2]
button = Class.Button(190, 565, 'Calculate')
scene2 = Class.Calculator(65,400,input_box1,input_box2,text4,text3)

while True:
    screen.fill((255,255,255))
    scene1.drawRect(screen)
    if not error:
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
                if float(input_box1.text)>=0 and float(input_box1.text)<=10 and float(input_box2.text)>=0 and float(input_box2.text)<=10:
                    u = scene2.calculate()
                    scene1.changeDistance(float(input_box2.text))
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
        for box in input_boxes:
            box.handleEvent(event)
            box.numberCheck()
        if event.type == pg.QUIT: 
            pg.quit()
            exit() 
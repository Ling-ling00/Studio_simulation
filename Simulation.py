import math
import pygame as pg
pg.init()

class Projectile:
    def __init__(self,x=0,y=0,s=0,u=0,a=(math.pi/3)):
        self.x = x #start position X
        self.y = y #start position Y
        self.s = s #size of dot
        self.u = u #start velocity
        self.a = a #angle in radian
        self.time = -1
        self.list = []
    def drawProjectile(self,screen):
        self.acceleration = 0.1962
        self.velocityX = self.u*math.cos(self.a)*2
        self.velocityY = self.u*math.sin(self.a)*2
        self.time += 1
        self.dx = int((self.velocityX*self.time))
        self.dy = int((self.velocityY*self.time)-(self.acceleration*(self.time**2)/2))
        pg.draw.circle(screen,(100,100,100),(self.x+self.dx,self.y-self.dy),self.s)
        self.list.append((self.x+self.dx, self.y-self.dy))
        for i in self.list:
            pg.draw.circle(screen,(0,0,100),(i[0],i[1]),int(self.s/5))
        if self.dy <= 0:
            self.time = 0
            self.list = []
    def changeVelocity(self, velocity):
        self.u = velocity

class Sanam:
    def __init__(self,x=0,y=0,distance=200):
        self.x = x
        self.y = y
        self.distance = distance+200
    def drawSanam(self,screen):
        pg.draw.line(screen,(100,100,100),(self.x+200,self.y),(self.x+200,self.y-200),1)
        pg.draw.rect(screen,(100,100,100),(self.x+(self.distance*2),self.y-70,26,70))
        pg.draw.polygon(screen, (100, 100, 100), ((self.x,self.y),(self.x,self.y-70),(self.x-44,self.y)))
    def changeDistance(self, distance):
        self.distance = distance+200

class TextBox:
    def __init__(self, x, y, text='', color=(0,0,0,)):
        self.color = color
        self.text = FONT.render(text, True, self.color)
        self.textRect = (x, y)
    def draw(self,screen):
        screen.blit(self.text, self.textRect)
    def changeText(self,text):
        self.text = FONT.render(text, True, self.color)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = inactiveColor
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = activeColor if self.active else inactiveColor
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def number_check(self):
        if(self.text[-1:].isnumeric()):
            pass
        else:
            self.text = self.text[:-1]
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Button:
    def __init__(self, x, y, text=''):
        self.color = inactiveColor
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.rect = pg.Rect(x, y, self.txt_surface.get_width()+10, self.txt_surface.get_height()+10)
        self.status = 0
    
    def isMousePress(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = activeColor
                self.txt_surface = FONT.render(self.text, True, self.color)
                return True
        self.color = inactiveColor
        self.txt_surface = FONT.render(self.text, True, self.color)
        return False
    
    def draw(self, Screen):
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)

class Calculate:
    def __init__(self, Sx = 0, Sy = 206.5):
        self.Sy = Sy+206.5
        self.Sx = Sx
    def changeDistance(self,Sx,Sy):
        self.Sy = Sy+206.5
        self.Sx = Sx
    def velocityCalculate(self):
        rad = 60 / 360 * 2 * math.pi
        u = math.sqrt((self.Sy*9.8/100)/math.sin(2*rad))
        print(u)
        return u
    def voltageCalculate(self):
        v = (self.Sy-0.6961)/0.6405
        return round(v, 2)
    def distanceXCalculate(self):
        x = self.Sx + 8.71
        return x

win_x, win_y = 800, 680
screen = pg.display.set_mode((win_x, win_y))
FONT = pg.font.Font(None, 32)
inactiveColor = (100,100,100)
activeColor = (0,0,0)

text1 = TextBox(75, 330, 'Xtarget =                           cm.')
text2 = TextBox(75, 380, 'Ytarget =                           cm.')
text3 = TextBox(425, 330, 'Xrobot  =  ___  cm.')
text4 = TextBox(425, 380, 'Voltage =  ___  V.')
text_boxes = [text1, text2, text3, text4]
input_box1 = InputBox(175, 325, 150, 32)
input_box2 = InputBox(175, 375, 150, 32)
input_boxes = [input_box1, input_box2]
button = Button(190, 425, 'Calculate')
squatBall = Projectile(150,220,5,0)
field = Sanam(150,290,0)
calculate = Calculate()
run = True

while run:
    screen.fill((255,255,255))
    if button.status == 1:
        squatBall.drawProjectile(screen)
        field.drawSanam(screen)
    button.draw(screen)
    for text in text_boxes:
        text.draw(screen)
    for box in input_boxes:
        box.draw(screen)
    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get(): # ทำการ Check event ต่างๆที่เกิดขึ้น
        for box in input_boxes:
            box.handle_event(event)
            box.number_check()
        if button.isMousePress(event) and input_box1.text != '' and input_box2.text != '':
            button.status = 1
            calculate.changeDistance(float(input_box1.text),float(input_box2.text))
            squatBall.changeVelocity(calculate.velocityCalculate())
            field.changeDistance(float(input_box2.text))
            returnText3 = 'Xrobot  = ' + str(calculate.distanceXCalculate()) + ' cm.'
            returnText4 = 'Voltage = ' + str(calculate.voltageCalculate()) + ' V.'
            text3.changeText(returnText3)
            text4.changeText(returnText4)
        if event.type == pg.QUIT: 
            pg.quit()
            exit()



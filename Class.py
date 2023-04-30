import math
import pygame as pg
pg.init()

FONT = pg.font.Font(None, 32)
inactiveColor = (100,100,100)
activeColor = (0,0,0)

class Simulation:
    def __init__(self, x, y, distance = 200, velocity = 0):
        self.__x = x
        self.__y = y
        self.status = False
        self.__distance = distance
        self.__velocity = velocity
        self.__time = 1
        self.__list = []
    def drawProjectile(self, size, screen):
        if self.status:
            self.__velocityX = self.__velocity*math.cos(math.pi/3)*2
            self.__velocityY = self.__velocity*math.sin(math.pi/3)*2
            self.__time += 1
            self.__dx = int((self.__velocityX*self.__time))
            self.__dy = int((self.__velocityY*self.__time)-(0.1962*(self.__time**2)/2))
            pg.draw.circle(screen,(100,100,100),(self.__x+self.__dx,self.__y-self.__dy), size)
            self.__list.append((self.__x+self.__dx, self.__y-self.__dy))
            for i in self.__list:
                pg.draw.circle(screen,(0,0,100),(i[0],i[1]),int(size/5))
            if self.__dy <= 0:
                self.__time = 0
                self.__list = []
    def drawField(self, screen):
        if self.status:
            pg.draw.line(screen,(100,100,100),(self.__x+200,self.__y+70),(self.__x+200,self.__y-200+70),1)
            pg.draw.rect(screen,(100,100,100),(self.__x+(self.__distance*2),self.__y,26,70))
            pg.draw.polygon(screen, (100, 100, 100), ((self.__x,self.__y+70),(self.__x,self.__y),(self.__x-44,self.__y+70)))
    def drawRect(self, screen):
        pg.draw.rect(screen,(100,100,100),(self.__x-54,self.__y-280,550,370),2)
    def changeVelocity(self, velocity):
        self.__velocity = velocity
    def changeDistance(self, distance):
        self.__distance = distance+200

class Calculator:
    def __init__(self, x, y, targetX, targetY, voltage, robotX):
        self.__x = x
        self.__y = y
        self.targetX = targetX
        self.targetY = targetY
        self.voltage = voltage
        self.robotX = robotX
    def calculate(self):
        rad = 60 / 360 * 2 * math.pi
        Sy = (float(self.targetY.text)+206.5)
        Sx = float(self.targetX.text)
        u = math.sqrt((Sy*9.8/100)/math.sin(2*rad))
        v = (Sy-0.6961)/0.6405
        x = Sx + 8.71
        returnText3 = 'Xrobot  = ' + str(x) + ' cm.'
        returnText4 = 'Voltage = ' + str(round(v,2)) + ' V.'
        self.robotX.changeText(returnText3)
        self.voltage.changeText(returnText4)
        return (u)
    def drawRect(self, screen):
        pg.draw.rect(screen,(100,100,100),(self.__x,self.__y,670,220),2)

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

    def handleEvent(self, event):
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
    
    def numberCheck(self):
        if(self.text[-1:].isnumeric()):
            pass
        else:
            self.text = self.text[:-1]
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

class Button:
    def __init__(self, x, y, text=''):
        self.color = inactiveColor
        self.text = text
        self.x = x
        self.y = y
        self.txt_surface = FONT.render(text, True, self.color)
        self.rect = pg.Rect(self.x, self.y, self.txt_surface.get_width()+10, self.txt_surface.get_height()+10)
        self.status = False
    
    def isMousePress(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = activeColor
                self.txt_surface = FONT.render(self.text, True, self.color)
                return True
        self.color = inactiveColor
        self.txt_surface = FONT.render(self.text, True, self.color)
        return False
    
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

import math
import pygame as pg
pg.init()

inactiveColor = (100,100,100)
activeColor = (0,0,0)

class MainWindow():
    def __init__(self, simulationWindow, calculatorWindow, manualWindow):
        self.__simulationWindow = simulationWindow
        self.__calculatorWindow = calculatorWindow
        self.__manualWindow = manualWindow
        self.__status = [0, 0, 0]
    def main(self, size, screen):
        if self.__manualWindow.status == 0:
            self.__simulationWindow.drawProjectile(size, screen)
            self.__calculatorWindow.draw(screen)
            self.__manualWindow.drawMain(screen)
            self.__simulationWindow.changeVelocity(self.__status[1])
            self.__simulationWindow.changeDistance(self.__status[2])
            self.__simulationWindow.status = self.__status[0]
        else:
            self.__manualWindow.draw(screen)
    def mainUpdateEvent(self, event):
        if self.__manualWindow.status == 0:
            self.__status = self.__calculatorWindow.updateEvent(event)
            self.__manualWindow.updateEventMain(event)
            print(self.__status[0])
        else:
            self.__manualWindow.updateEvent(event)

class Simulation:
    def __init__(self, x, y):
        self.__x = x+115
        self.__y = y+270
        self.status = 0
        self.__distance = 193.5
        self.__velocity = 0
        self.__time = 1
        self.__list = []

    def drawProjectile(self, size, screen):
        self.text6 = TextBox(self.__x-105, self.__y-255, 'Simulation', fontSize = 48)
        self.text6.draw(screen)
        pg.draw.rect(screen,(100,100,100),(self.__x-115,self.__y-270,670,370),2)
        if self.status == 1:
            self.text1 = TextBox(self.__x+72, self.__y+67, '100.00 cm.', fontSize= 18)
            self.text2 = TextBox(self.__x+self.__distance+86, self.__y+67, '%.2f' %(self.__distance-100+6.50)+' cm.',fontSize= 18)
            pg.draw.line(screen,(100,100,100),(self.__x+200,self.__y+70),(self.__x+200,self.__y-200+70),1)
            pg.draw.rect(screen,(100,100,100),(self.__x+(self.__distance*2),self.__y,26,70))
            pg.draw.polygon(screen, (100, 100, 100), ((self.__x,self.__y+70),(self.__x,self.__y),(self.__x-44,self.__y+70)))
            pg.draw.line(screen,(100,100,100), (self.__x, self.__y+80), ((self.__x+(self.__distance*2)+13), self.__y+80))
            pg.draw.line(screen,(100,100,100), (self.__x, self.__y+75), (self.__x, self.__y+85))
            pg.draw.line(screen,(100,100,100), ((self.__x+(self.__distance*2)+13), self.__y+75), ((self.__x+(self.__distance*2)+13), self.__y+85))
            pg.draw.line(screen,(100,100,100), (self.__x+200, self.__y+75), (self.__x+200, self.__y+85))
            self.text1.draw(screen)
            self.text2.draw(screen)

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
        if self.status == 2:
            self.text3 = TextBox(self.__x+45, self.__y-90 , 'Please enter number!!', (255,0,0), 48)
            self.text3.draw(screen)
        if self.status == 3:
            self.text4 = TextBox(self.__x+45, self.__y-90 , 'Number not in range!!', (255,0,0), 48)
            self.text4.draw(screen)

    def changeVelocity(self, velocity):
        self.__velocity = velocity

    def changeDistance(self, distance):
        self.__distance = distance+193.5

class Calculator:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.targetX = InputBox(self.__x+110, self.__y+65, 150, 32)
        self.targetY = InputBox(self.__x+110, self.__y+115, 150, 32)
        self.voltage = TextBox(self.__x+360, self.__y+120, 'Voltage =  ___  V.')
        self.robotX = TextBox(self.__x+360, self.__y+70, 'Xrobot  =  ___  cm.')
        self.text1 = TextBox(self.__x+10, self.__y+70, 'Xtarget =                           cm.')
        self.text2 = TextBox(self.__x+10, self.__y+120, 'Ytarget =                           cm.')
        self.text3 = TextBox(self.__x+10, self.__y+15, 'Calculator',fontSize = 48)
        self.text4 = TextBox(self.__x+10, self.__y+100, 'Please enter number between 0.00 - 50.00', (100,100,100), 18)
        self.text5 = TextBox(self.__x+10, self.__y+150, 'Please enter number between 6.50 - 30.30', (100,100,100), 18)
        self.textBoxes = [self.text1, self.text2, self.text3, self.text4, self.text5, self.voltage, self.robotX]
        self.inputBoxes = [self.targetX, self.targetY]
        self.button = Button(self.__x+120, self.__y+170, 'Calculate')
        self.__status = 0
        self.u = 0
        self.d = 200
    def draw(self, screen):
        pg.draw.rect(screen,(100,100,100),(self.__x,self.__y,670,220),2)
        self.button.draw(screen)
        for i in self.textBoxes:
            i.draw(screen)
        for i in self.inputBoxes:
            i.draw(screen)
    def updateEvent(self,event):
        for box in self.inputBoxes:
            box.handleEvent(event)
            box.numberCheck()
        if self.button.isMousePress(event):
            if self.targetX.text != '' and self.targetY.text != '':
                if float(self.targetX.text)>=0 and float(self.targetX.text)<=50 and float(self.targetY.text)>=6.5 and float(self.targetY.text)<=30.3:
                    rad = 60 / 360 * 2 * math.pi
                    Sy = (float(self.targetY.text)+200)
                    Sx = float(self.targetX.text)
                    self.u = math.sqrt((Sy*9.8/100)/math.sin(2*rad))
                    v = (1.5575*Sy)-1.552 #voltage
                    x = Sx - 0.93 + 15 #distanceX
                    returnText3 = 'Xrobot  = ' + str(round(x,1)) + ' cm.'
                    returnText4 = 'Voltage = ' + str(int(v)) + ' V.'
                    self.robotX.changeText(returnText3)
                    self.voltage.changeText(returnText4)
                    self.d = float(self.targetY.text)
                    self.__status = 1
                    self.button.status = True
                else:
                    self.__status = 3
            else:
                self.__status = 2
        return (self.__status,self.u,self.d)

class Manual:
    def __init__(self, img, x, y):
        self.__x = x
        self.__y = y
        self.__img = []
        self.next = Button(self.__x+700, self.__y+600, 'next', 32)
        self.back = Button(self.__x+30, self.__y+600, 'back', 32)
        self.manual = Button(self.__x+644, self.__y+20, 'manual', 32)
        self.close = Button(self.__x+750, self.__y+20, 'X', 32, (255,0,0))
        self.i = 0
        self.status = 0
        for i in img:
            imp = pg.image.load(i).convert()
            self.__img.append(imp)
    def draw(self, screen):
        if self.i == 0:
            screen.blit(self.__img[self.i], (self.__x,self.__y))
            self.next.draw(screen)
            self.close.draw(screen)
        elif self.i < len(self.__img)-1:
            screen.blit(self.__img[self.i], (self.__x,self.__y))
            self.next.draw(screen)
            self.back.draw(screen)
            self.close.draw(screen)
        else:
            screen.blit(self.__img[self.i], (self.__x,self.__y))
            self.back.draw(screen)
            self.close.draw(screen)
    def updateEvent(self,event):
        if self.i == 0:
            if self.next.isMousePress(event):
                self.i += 1
        elif self.i < len(self.__img)-1:
            if self.next.isMousePress(event):
                self.i += 1
            if self.back.isMousePress(event):
                self.i -= 1
        else:
            if self.back.isMousePress(event):
                self.i -= 1
        if self.close.isMousePress(event):
            self.status = 0
            self.i = 0
    def updateEventMain(self,event):
        if self.manual.isMousePress(event):
            self.status = 1
    def drawMain(self, screen):
        self.manual.draw(screen)

class TextBox:
    def __init__(self, x, y, text='', color=(0,0,0,), fontSize = 32):
        self.color = color
        self.font = pg.font.Font(None, fontSize)
        self.text = self.font.render(text, True, self.color)
        self.textRect = (x, y)
    def draw(self,screen):
        screen.blit(self.text, self.textRect)
    def changeText(self,text):
        self.text = self.font.render(text, True, self.color)

class InputBox:
    def __init__(self, x, y, w, h, text='', fontSize = 32):
        self.rect = pg.Rect(x, y, w, h)
        self.color = inactiveColor
        self.text = text
        self.font = pg.font.Font(None, fontSize)
        self.txt_surface = self.font.render(text, True, self.color)
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
                self.txt_surface = self.font.render(self.text, True, self.color)
    
    def numberCheck(self):
        if(self.text[-1:].isnumeric() or self.text[-1:] == '.'):
            pass
        else:
            self.text = self.text[:-1]
            self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

class Button:
    def __init__(self, x, y, text='', fontSize = 32, inactiveColor = inactiveColor, activeColor = activeColor):
        self.inactiveColor = inactiveColor
        self.activeColor = activeColor
        self.color = self.inactiveColor
        self.text = text
        self.x = x
        self.y = y
        self.font = pg.font.Font(None, fontSize)
        self.txt_surface = self.font.render(text, True, self.color)
        self.rect = pg.Rect(self.x, self.y, self.txt_surface.get_width()+10, self.txt_surface.get_height()+10)
        self.status = False
    
    def isMousePress(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = self.activeColor
                self.txt_surface = self.font.render(self.text, True, self.color)
                return True
        self.color = self.inactiveColor
        self.txt_surface = self.font.render(self.text, True, self.color)
        return False
    
    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

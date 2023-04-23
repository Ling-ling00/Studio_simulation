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

class Sanam:
    def __init__(self,x=0,y=0,distance=0):
        self.x = x
        self.y = y
        self.distance = distance
    def drawSanam(self,screen):
        pg.draw.line(screen,(100,100,100),(self.x+200,self.y),(self.x+200,self.y-200),1)
        pg.draw.rect(screen,(100,100,100),(self.x+(self.distance*200),self.y-70,26,70))
        pg.draw.polygon(screen, (100, 100, 100), ((self.x,self.y),(self.x,self.y-70),(self.x-44,self.y)))

win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
squatBall = Projectile(100,400,5,5.18)
field = Sanam(100,470,2.3)
run = True

while run:
    screen.fill((255,255,255))
    squatBall.drawProjectile(screen)
    field.drawSanam(screen)
    pg.time.delay(10)
    pg.display.update()

    for event in pg.event.get(): # ทำการ Check event ต่างๆที่เกิดขึ้น
        if event.type == pg.QUIT: 
            pg.quit()
            exit()



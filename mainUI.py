import pygame
from random import randint

WHITE = 255, 255, 255
GREY = 128, 128, 128
GREEN = 0, 255, 0
RED = 255, 0, 0
pygame.font.init()




class Chart:
    def __init__(self,names) -> None:
        self.values = [i for i in range(1,101)] 
        self.buttons = [Button(name) for name in names] 
 
    def drawChart(self,screen):
        pygame.draw.rect(screen,GREY,((0,0),(600,600)),0)
        for i in range(100):
            drawBar(screen,self.values)
    
    def shuffleChart(self):
        for i in range(100):
            self.values[i] = randint(1,101)*5
    
    def drawButtons(self, screen):
        fnt = pygame.font.SysFont("comicsans", 40)
        for i in range(5):
            pygame.draw.rect(screen,((0,100,200)),((0,602+i*50),(600,48)))
            text = fnt.render(self.buttons[i].name, 1, (228,228,228))
            screen.blit(text,((300-text.get_width()/2),(602+i*50+text.get_height()/2)))

            if self.buttons[i].selected:
                points = ((0,600+i*50),(600,600+i*50),(600,650+i*50),(0,650+i*50))
                pygame.draw.lines(screen,GREEN,True,points,width=3)


    def click(self, pos):
        if pos[0] < 600 and pos[1] > 600:
            y = (pos[1]-600) // 50
            return y+1
        else:
            return None

    def select(self, y):
        for i in range(5):
            self.buttons[i].selected = False
        self.buttons[y-1].selected = True

class Button:
    def __init__(self,name) -> None:
        self.name = name
        self.selected = False
        
def draw(screen,chart):
    screen.fill(WHITE)
    chart.drawChart(screen)
    chart.drawButtons(screen)
    pygame.display.update()

def drawBar(screen,values,clearBg=False,colors={}):
    if clearBg:
        pygame.draw.rect(screen,GREY,((0,0),(600,600)))
    for i in range(100):
        color = 255, 255, 0
        if i in colors:
            color = colors[i]
        pygame.draw.rect(screen,color,((i*5+40,600-values[i]),(4,values[i])))
        
    if clearBg:
        pygame.display.update()
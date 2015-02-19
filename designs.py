from graphics import *
from myWin import *
import sys


def circularEffects2(win, cList, xSkip=19, ySkip=17,
                     radius=15, width=250, height=250, xstart = 0, ystart = 0):
    for x in range(xstart, width+20, xSkip):
        for y in range(ystart, height+20, ySkip):
            cir = Circle(Point(x,y),radius)
            
            if (x+y)%2 == 0:  #Only half the circles in this effect are colored
                cir.setOutline(cList[((x+y)//10)% len(cList)])
                
            win.draw(cir)

    return win

def vEffects2(win, cList, xSkip=19, ySkip=17, radius=15,
              width=250, height=250, xstart = 0, ystart = 0):
    for x in range(xstart, width+20, xSkip):
        for y in range(ystart, height+20, ySkip):
            cir = Circle(Point(x,y),radius)

            if (x+y)%2 == 0:
                cir.setOutline(cList[((x+y)//10)% len(cList)])
            else:
                cir.setOutline(cList[((x+y)//3)% len(cList)])
            
            win.draw(cir)

    return win


def circularEffects(win, cList, xSkip=19, ySkip=17,
                     radius=15, width=250, height=250,
                     xstart = 0, ystart = 0):
    for x in range(xstart, width+20, xSkip):
        for y in range(ystart, height+20, ySkip):
            cir = Circle(Point(x,y),radius)
            cir.setOutline(cList[(x+y)% len(cList)])
            win.draw(cir)
    return win

                

def rectangularEffects(win, cList, xSkip = 19, ySkip = 17,
                       size = 15, isDiamond = True, width=250,
                       height=250, xstart = 0, ystart=0):
    for x in range(xstart, width+20, xSkip):
        for y in range(ystart, height+20, ySkip):
            if isDiamond:
                shape = Diamond(Point(x,y),size)

            else:
                shape = Square(Point(x,y),size)
            shape.setOutline(cList[((x+y)//10)% len(cList)])
            win.draw(shape)
    return win

def diamondWorld(win,colorList, width=250, height=250, xstart = 0, ystart = 0):
    return rectangularEffects(win, colorList, 15, 12, 40, True,width,height,xstart,ystart)


def stairs(win,colorList, width=250, height=250, xstart = 0, ystart = 0):    
    return rectangularEffects(win, colorList, 9, 13, 25, False,width,height,xstart,ystart)


def wave(win,colorList, width=250, height=250, xstart = 0, ystart = 0):
    circularEffects2(win,colorList,19,17,6,width,height,xstart,ystart)
    circularEffects2(win,colorList,19,17,12,width,height,xstart,ystart)
    circularEffects2(win,colorList,19,17,3,width,height,xstart,ystart)
    circularEffects2(win,colorList,19,17,9,width,height,xstart,ystart)
    circularEffects2(win,colorList,19,17,15,width,height,xstart,ystart)
    return win
    
def bubbleWorld(win,colorList, width=250, height=250, xstart = 0, ystart = 0):
    circularEffects2(win,colorList,15,15,8,width,height,xstart,ystart)
    circularEffects2(win,colorList,20,20,4,width,height,xstart,ystart)
    return win

def bubbleWorld2(win,colorList, width=250, height=250, xstart = 0, ystart = 0):
    circularEffects2(win,colorList,15,15,8,width,height,xstart,ystart)
    circularEffects2(win,colorList,20,20,4,width,height,xstart,ystart)
    circularEffects2(win,colorList,13,17,4,width,height,xstart,ystart)
    return win


def vWave(win, colorList, width=250, height=250, xstart = 0, ystart = 0):
    vEffects2(win,colorList,19,17,6,width,height,xstart,ystart)
    vEffects2(win,colorList,19,17,12,width,height,xstart,ystart)
    vEffects2(win,colorList,19,17,3,width,height,xstart,ystart)
    vEffects2(win,colorList,19,17,9,width,height,xstart,ystart)
    vEffects2(win,colorList,19,17,15,width,height,xstart,ystart)
    return win

def cloverField(win, colorList, width = 250, height = 250, xstart = 0, ystart = 0):
    for i in range(3):
        circularEffects(win,colorList,10,10,10-i,width,height,xstart,ystart)
    return win


def Square(center, size):    
    bottom = center.clone()
    center.move(size//2, size//2)#center is treated as the top
    bottom.move(size//-2, size//-2)
    return Rectangle(center,bottom)

def Diamond(center, size):
    bottom = center.clone()
    left = center.clone()
    right = center.clone()

    center.move(0,size//-2) #center is treated as the top
    bottom.move(0,size//2)
    left.move(size//-2,0)
    right.move(size//2,0)

    return Polygon(center,left,bottom,right)


def main(width=250, height=500):
    if len(sys.argv) >= 3:
        width = int(sys.argv[1])
        height = int(sys.argv[1])
        
    colorListA = ["blue","green","cyan","purple"]
    colorListB = ["blue","green","red"]
    colorListV = ["yellow","purple","red"]
    winList = []
    
    winList.append(bubbleWorld(myWin("Bubble World",width,height),colorListB,width,height))
    winList.append(wave(myWin("RGB Wave",width,height),colorListB,width,height))
    winList.append(wave(myWin("Ocean Floor",width,height),colorListA,width,height))
    winList.append(stairs(myWin("Stairs",width,height),colorListA,width,height))
    winList.append(diamondWorld(myWin("Glittering Prizes",width,height),colorListA,width,height))
    winList.append(vWave(myWin("Victoria's Wave", width, height,"black"),colorListV, width, height))   
    winList.append(bubbleWorld2(myWin("Bubble 2", width, height, "orange"),colorListA,width,height))

    totalShapes = 0

    for eachWin in winList:
        totalShapes += eachWin.getShapeCount()


    print("Total Shapes:  \t%7i"%totalShapes)

if __name__ == "__main__":
    main()

from graphics import *

"""
A powerful extension of the Graphics window that keeps track of
the shapes inside of it.
"""
class myWin:
    def __init__(self,title = "untitled", width=250,
                 height=250, bgColor ="White", shapes = None):
        self.title = title
        self.width = width
        self.height = height
        self.bgColor = bgColor #background color
        if shapes == None:
            self.shapes = []
        else:
            self.shapes = shapes #A list of all shapes in the image
        self.win = self.__construct() #underlying window
            
            

    #Creates the window and sets the bgColor
    def __construct(self):
        win = GraphWin(self.title,self.width,self.height)
        win.setBackground(self.bgColor)
        for eachShape in self.shapes:
            eachShape.draw(win)
        return win
    """
Because there's no way to change the attributes of an existing
Graphwin object, when I need to change the attributes of a myWin
I delete the underlying Graphwin and repopulate it using the
underlying shapes List.
    """
    def __reconstruct(self):
        self.win.close()
        self.win = self.__construct()
    

    def draw(self, shape):
        self.shapes.append(shape)
        shape.draw(self.win)

    def getTitle(self):
        return self.title

    def isClosed(self):
        return self.win.isClosed()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getBgColor(self):
        return self.bgColor

    def getShapeCount(self):
        return len(self.shapes)

    def getShapes(self):
        return self.shapes

    def setShapes(self,shapesList):
        self.shapes = shapesList
    
    def setTitle(self, title):
        self.title = title
        self.__reconstruct()

    def setWidth(self, width):
        self.width = width
        self.__reconstruct()

    def setHeight(self, height):
        self.height = height
        self.__reconstruct()

    def setBgColor(self, bgColor):
        self.bgColor = bgColor
        self.__reconstruct()

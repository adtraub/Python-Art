#Main
#A text based front end to the shapes of math project
#Adam Traub
#6/5/2010

from designs import *
from sys import version

if version[0] == '3':
    raw_input = input


#The first few functions are simply menus
def intro():
    return """
Welcome to the Shapes of Math project.  This projects was created by Adam Traub
largely thanks to John Zelle and his Graphics package.  With this program, you
will be able to create your own designs and view some of my favorites.  This
program was created to better understand Zelle's graphic package in order to
aid me in my undergraduate teaching assistant postion at Randolph-Macon College.
"""


def menu():
    return"""

Main Menu:
1.) View a predefined art piece
2.) Create your own art piece
3.) Change width and height of Art Window
4.) About...
ANY OTHER VALUE.) Quit

Choice: """


#By passing in the predefined functions list,
#this function creates a dynamic menu for predefined art pieces
def betterArtMenu(preDefinedFunctions):
    retString = """

Predefined art menu
Which image would you like to see?"""
    for i in range(len(preDefinedFunctions)):
        retString += "\n%d.) %s"%(i+1,preDefinedFunctions[i][0])
    retString+=""" (favorite!)
ANY OTHER VALUE.) Cancel

Choice: """
    return retString
    
def shapesMenu(layer):
    return"""

What shape would you like to use on layer %d:
1.) Circles
2.) Squares
3.) Diamonds

Remember, type the number, not the word!

choice: """%(layer + 1)

def layerDialog():
    return"""

These images are created by creating several layers of shapes that
sit on top of one another.  First, we must decide how many layers
you'd like.  2-4 usually works well.

Total Layers: """

#a dynamic menu for the colors.
def colorMenu():
    retString = ""
    colors = getColors()
    for i in range(len(colors)):
        retString+="%2d.) %s\n"%((i+1),colors[i])
    return retString

#The list of available colors
def getColors():
    return["red","orange","yellow","green","blue",
           "purple","cyan","pink","black","white"]

#A simple function to prompt the user for an int that
#will also handle improper input with recursion
def getIntInput(message = "Enter an int", 
                errorMessage = "You must type a whole number\n"):
    try:
        return int(raw_input(message))

    except ValueError:
        print(errorMessage)
        return getIntInput(message, errorMessage)

#A simple utility that sets a range of acceptable values
#If cal is outside that range, it is put inside    
def adjustAccordingly(val,low,high):
    if val < low:
        val = low
    elif val > high:
        val = high

    return val

#The function associated with creating a custom design
def createDesigns(width,height):
    colorList = []#A list of chosen colors for the design
    dataList  = []#A list that holds the data associated with the size, spacing, and shape type.
    colors = getColors()

    layerCount = getIntInput(layerDialog())

    print("\nFor spacing, 20 tends to be a fine number, but experiment with it!")
    print("For sizing, 15 is a good number, but remeber, this is your art!")
    print("For any value, 2 is the minimum, 200 is the max")
    raw_input("Press enter to continue")

    for i in range(layerCount):
        xWidth = getIntInput("\n\nHow far should the shapes be spaced horizontally on layer "+str(i+1)+": ")
        yWidth = getIntInput("How far should the shapes be spaced vertically on layer "+str(i+1)+": ")
        size = getIntInput("How big should the shapes be on layer "+str(i+1)+": ")
        shapeType = getIntInput(shapesMenu(i))
        shapeType = adjustAccordingly(shapeType,0,3)
        dataList.append([xWidth,yWidth,size,shapeType])
        for vals in dataList[-1]:
            vals = adjustAccordingly(vals,2,200)


    colorDialog = colorMenu() #The color menu string
    while True:
        print("Please choose a color")
        print(colorDialog)
        print("Type -1 when finished choosing colors")
        addColor = getIntInput("Choice: ")
        if addColor == -1:
            break
        else:
            addColor -= 1
            addColor = adjustAccordingly(addColor,0,len(colors)-1)
            colorList.append(colors[addColor])

    print("What would you like to use as a background color?\n"+colorDialog)    
    addColor = getIntInput("Choice: ")-1
    addColor = adjustAccordingly(addColor,0,len(colors)-1)
    bgColor = colors[addColor]

    title = raw_input("What will you name this art project: ")
    raw_input("Press enter to create your design")


    win = myWin(title,width,height,bgColor)
    for i in range(layerCount):
        xWidth = dataList[i][0]
        yWidth = dataList[i][1]
        size   = dataList[i][2]
        if dataList[i][3] == 1:
            circularEffects(win,colorList,xWidth,yWidth,size,width,height)
        if dataList[i][3] == 2:
            rectangularEffects(win,colorList,xWidth,yWidth,size,False,width,height)
        if dataList[i][3] == 3:
            rectangularEffects(win,colorList,xWidth,yWidth,size,True,width,height)

    raw_input("This is your art!  Sorry you can't save it,\n"+
          "but you can take a screenshot!")
    return win
        
"""
Because everything in python is an object, including functions, I'm able to
put all of the predefined functions into a list.  I then give the user a menu
prompting him for a value that is associated with one of the values.  The
value the user provides is then used to index the list of function objects and
runs the function.
"""
def predefinedImages(width,height,preDefinedFunctions):
    preDefChoice = getIntInput(betterArtMenu(preDefinedFunctions))-1
    
    if not 0 <= preDefChoice < len(preDefinedFunctions):
        return None
            
    toDraw = preDefinedFunctions[preDefChoice]
    
    if len(toDraw) == 3:
        win = myWin(toDraw[0],width,height)
    else:
        win = myWin(toDraw[0], width, height, toDraw[3])
        
    toDraw[1].__call__(win,toDraw[2],width,height)
    return win
    
    
def main():
    width = 500#default window width
    height = 500#default window height
    """
    pictureQ holds all the previous art windows that were created.
    This is done because the windows will freeze if they are dereferenced."""
    pictureQ = []

    #A list of all predefined functions
    #The list holds Window title, function, colorList,
    #and background Color if applicable
    preDefinedFunctions = [("BubbleWorld",bubbleWorld,["blue","green","red"]),
                           ("RGB Wave", wave,["blue","green","red"]),
                           ("Ovean Floor",wave,["blue","green","cyan","purple"]),
                           ("Stairs",stairs,["blue","green","cyan","purple"]),
                           ("Glittering Prizes",diamondWorld,["blue","green","cyan","purple"]),
                           ("Victoria's Wave",vWave,["yellow","purple","red"],"black"),
                           ("Cloverfield",cloverField,["red","orange","yellow","yellow","green","blue","purple"])]    
    print(intro())
    while True:
        choice = raw_input(menu())
        #view a predefined image
        if choice == "1":
            pictureQ.append(predefinedImages(width,height,preDefinedFunctions))

        #create your own art piece
        elif choice == "2":
            pictureQ.append(createDesigns(width,height))

        #simply changes the width and height of the window
        elif choice == "3":
            print("Current width: %d"%(width))
            width = adjustAccordingly(getIntInput("New width: "),10,99999)
            print("\nCurrent height: %d"%(height))
            height=adjustAccordingly(getIntInput("New height: "),10,99999)

        #Repeat intro
        elif choice == "4":
            print(intro())

        #Quit
        else:
            print("Are you sure you want to quit? (y/n)")
            uChoice = raw_input("choice: ")
            if uChoice.lower() in ["y","yes"]:
                return
                
        raw_input("Press enter to continue")
                
                
if __name__ == "__main__":
    import sys
    sys.exit(main())

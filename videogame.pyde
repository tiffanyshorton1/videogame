xCoordinate = random(0,300)
yCoordinate = random(60,340)
xSpeed = 2
ySpeed = 2
b1 = True
b2 = True
b3 = True
b4 = True
b5 = True 
b6 = True
brick = "go"

def setup():
    size(600,400)
    background(0)
    
    
def draw():
    global xCoordinate, yCoordinate, xSpeed, ySpeed, b1, b2, b3, b4, b5, b6, brick       #calls variable from gloabl scope
    size = 15
    hEdge = size/2
    vEdge = size/2
    
                                                          #redraws background to cover circle
    background(0)
    
    noStroke()
    if b1 == False:
        fill(0)
    else:
        fill("#5676f6")
    rect(0,0,100,50)
    if b2 == False:
        fill(0)
    else:
        fill("#ebcf97")
    rect(100,0,100,50)
    if b3 == False:
        fill(0)
    else:
        fill("#153e4c")
    rect(200,0,100,50)
    if b4 == False:
        fill(0)
    else:
        fill("#c932b2")
    rect(300,0,100,50)
    if b5 == False:
        fill(0)
    else:
        fill("#19ccfc")
    rect(400,0,100,50)
    if b6 == False:
        fill(0)
    else:
        fill("#09cc87")
    rect(500,0,100,50)
    
                                                          #establishs new circle
    fill(255)
    xCoordinate += xSpeed                                 #+= shorthand to add a value to the original
    yCoordinate += ySpeed
    if brick == "go":
        print(xCoordinate, yCoordinate)
        ellipse(xCoordinate,yCoordinate,size,size)

                                                          #establishs condition to reset xCoordinate at the ends of the screen
    if xCoordinate >= 600-hEdge or xCoordinate <= hEdge:
        xSpeed = -xSpeed
        
    if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge <= 50:
        if b1 == True:
            b1 = False
            ySpeed = -ySpeed
        if b1 == False:
            if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    
    if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge <= 50:
        if b2 == True:
            b2 = False
        if b2 == False:
            if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

        
    if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge <= 50:
        if b3 == True:
            b3 = False
        if b3 == False:
            if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    
    if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge <= 50:
        if b4 == True:
            b4 = False
        if b4 == False:
            if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

        
    if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge <= 50:
        if b5 == True:
            b5 = False
        if b5 == False:
            if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

        
    if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge <= 50:
        if b6 == True:
            b6 = False
        if b6 == False:
            if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    
    fill(255)
    rect(mouseX, 370, 90, 5)
    
    if yCoordinate + vEdge >= 370 and xCoordinate - vEdge >= mouseX and xCoordinate + vEdge <= mouseX + 90:
        ySpeed= -ySpeed
        
    if yCoordinate >= 400:
        textSize (50)
        text("GAME OVER ALREADY?", 27, 150)
        brick = "stop"

    if b1 == False and b2 == False and b3 == False and b4 == False and b5 == False and b6 == False:
        textSize (50)
        stroke(255, 102, 90)
        text("YOU'RE A WINNER", 77,150)
        brick = "stop"
    

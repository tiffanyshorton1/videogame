#Coordinates for the ellipse
xCoordinate = random(10,300) 
yCoordinate = random(60,340)


#Changes the speed of the ball
xSpeed = 2
ySpeed = 2


#Variables assigned to each brick that determines visability
b1 = True
b2 = True
b3 = True
b4 = True
b5 = True 
b6 = True
b7 = True
b8 = True
b9 = True
b10 = True
b11 = True
b12 = True


#Variable that enables/disables the motion of the ball
ball = "stop"
game = "start"

#score variable
score = 0

#basic background
def setup():
    size(600,400)
    background(0)
    
#Everything that moves
def draw():
    #calls variables from global scope
    global xCoordinate, yCoordinate, xSpeed, ySpeed, game 
    global b1, b2, b3, b4, b5, b6, ball, score, b7, b8, b9, b10, b11, b12
    
    
    
    
    #Size variable sets the size of the ellipse; Edge variables help determine the outermost coordinates of the ball
    size = 15
    hEdge = size/2
    vEdge = size/2
    
    #redraws background to cover circle
    background(0)
    
    if game == "start":
        fill(255,0,0)
        rect(225, 200, 150, 50)
        fill(255)
        text("START", 224, 242)

    
    #score rectangle
    strokeWeight(2)
    stroke("#DBC677")
    noFill()
    rect(1,348,60,50)
    fill(255)
    textSize(48)
    if score <=9:
        text(score, 16, 392)
    elif score >= 10:
        text(score, 0,392)
    
    
    #Determines the visability of the bricks
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
    
    #Row 2
    if b7 == False:
        fill(0)
    else:
        fill("#887b95")
    rect(0,50,100,50)
    
    if b8 == False:
        fill(0)
    else:
        fill("#9890e4")
    rect(100,50,100,50)
    
    if b9 == False:
        fill(0)
    else:
        fill("#59bcd4")
    rect(200,50,100,50)
    
    if b10 == False:
        fill(0)
    else:
        fill(210,40,63)
    rect(300,50,100,50)
    
    if b11 == False:
        fill(0)
    else:
        fill("#7b1779")
    rect(400,50,100,50)
    
    if b12 == False:
        fill(0)
    else:
        fill("#f18ad3")
    rect(500,50,100,50)
    
    #establishs movement of circle
    fill(random(255),random(255),random(255))
    
    if ball == "go":
        xCoordinate += xSpeed                 
        yCoordinate += ySpeed
        ellipse(xCoordinate,yCoordinate,size,size)


    #establishs condition to reset xCoordinate at the ends of the screen
    if xCoordinate >= 600-hEdge or xCoordinate <= hEdge:
        xSpeed = -xSpeed
        
    
    #Bricks disappear when hit, ball bounces off of brick and top of screen when brick is not visible
    if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge <= 50:
        if b1 == True:
            b1 = False
            ySpeed = -ySpeed
            score += 2
        if b1 == False:
            if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge <= 50:
        if b2 == True:
            b2 = False
            ySpeed = -ySpeed
            score += 2
        if b2 == False:
            if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge <= 50:
        if b3 == True:
            b3 = False
            ySpeed = -ySpeed
            score += 2
        if b3 == False:
            if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed
                
    if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge <= 50:
        if b4 == True:
            b4 = False
            ySpeed = -ySpeed
            score += 2
        if b4 == False:
            if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge <= 50:
        if b5 == True:
            b5 = False
            ySpeed = -ySpeed
            score += 2
        if b5 == False:
            if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed

    if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge <= 50:
        if b6 == True:
            b6 = False
            ySpeed = -ySpeed
            score += 2
        if b6 == False:
            if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge <= 0:
                ySpeed = -ySpeed
                
    #Row 2
    if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100:
        if b7 == True:
            b7 = False
            ySpeed = -ySpeed
            score += 1
        if b7 == False:
            if xCoordinate + vEdge > 0 and xCoordinate - vEdge <= 100 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed

    if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100 :
        if b8 == True:
            b8 = False
            ySpeed = -ySpeed
            score += 1
        if b8 == False:
            if xCoordinate + vEdge > 100 and xCoordinate - vEdge <= 200 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed

    if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100:
        if b9 == True:
            b9 = False
            ySpeed = -ySpeed
            score += 1
        if b9 == False:
            if xCoordinate + vEdge > 200 and xCoordinate - vEdge <= 300 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed
                
    if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100:
        if b10 == True:
            b10 = False
            ySpeed = -ySpeed
            score += 1
        if b10 == False:
            if xCoordinate + vEdge > 300 and xCoordinate - vEdge <= 400 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed

    if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100:
        if b11 == True:
            b11 = False
            ySpeed = -ySpeed
            score += 1
        if b11 == False:
            if xCoordinate + vEdge > 400 and xCoordinate - vEdge <= 500 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed

    if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge > 50 and yCoordinate - vEdge <= 100 :
        if b12 == True:
            b12 = False
            ySpeed = -ySpeed
            score += 1
        if b12 == False:
            if xCoordinate + vEdge > 500 and xCoordinate - vEdge <= 600 and yCoordinate - vEdge > 50:
                ySpeed = ySpeed
                
                
    #creates paddle
    fill(255)
    rect(mouseX, 340, 90, 5)
    
    
    #Makes paddle move with mouse
    if yCoordinate + vEdge >= 340 and xCoordinate - vEdge >= mouseX and xCoordinate + vEdge <= mouseX + 90:
        ySpeed= -ySpeed
            
    #Fail message
    if yCoordinate >= 400:
        textSize (50)
        text("GAME OVER ALREADY?", 27, 150)
        ball = "stop"


    #Win message
    if b1 == False and b2 == False and b3 == False and b4 == False and b5 == False and b6 == False:
        textSize (50)
        stroke(255, 102, 90)
        text("YOU'RE A WINNER", 77,150)
        ball = "stop"
        
def mouseClicked():
    if mouseX >= 225 and mouseX <= 375 and mouseY >= 200 and mouseY <= 250:
        print("stuff")
        game = "going"
        ball = "go"
    

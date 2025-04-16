from cmu_graphics import *
def onAppStart(app):
    app.stepsPerSecond = 40
    app.height = 600
    app.width = 800
    app.receptorActive = False
    app.lx = 0
    app.ly = 0
    app.ligandMoving = True
    app.drawReceptorActive = False
    app.steps = 0
    app.animationActive = False
    app.connectorWidth = 40
def drawPhospholipid(app, cx, cy, orientation):
    r = 20
    #Draw the two tails of the phospholipid:
    drawLine(cx - r/2, cy, cx - r/2, cy + 50*orientation, fill='gray', lineWidth=3)
    drawLine(cx + r/2, cy, cx + r/2, cy + 50*orientation, fill='gray',lineWidth=3)
    #Draw the head of the phospholipid:
    drawCircle(cx, cy, r, fill='gray')

def drawTransmembraneReceptor(app, startX, startY):
    x = startX
    y = startY
    width = 40
    height = 30
    segmentHeight = 150
    drawLine(x - width/3, y - height/2, x - width/3, y, fill='purple', lineWidth=6)
    drawLine(x + width/3, y - height/2, x + width/3, y, fill='purple', lineWidth=6)
    drawLine(x - width/3 - 3, y, x + width/3 + 3, y, fill='purple', lineWidth=6)
    drawLine(x, y, x, y + segmentHeight, lineWidth = 8, fill='purple')
    drawLine(x - 4, y + segmentHeight, x + 44, y + segmentHeight, fill='purple', lineWidth=6)
    drawLine(x + 40, y, x + 40, y + segmentHeight, lineWidth = 8, fill='purple')
    drawLine(x + 36, y, x + 84, y, fill='purple', lineWidth=6)
    #new segment, veritcally, and extra long.
    drawLine(x + 80, y, x + 80, y + segmentHeight * 1.4, lineWidth = 8, fill='purple')
    #now: we draw the part that moves later, which will still be a series of lines, but have app variables stored that 
    drawLine(x + 76, y + segmentHeight * 1.4, x + 124, y + segmentHeight * 1.4, lineWidth = 8, fill='green')
    #here, draw the part after the changing part, that will not change despite activity
    thisSpecificLineLength = segmentHeight * 1.4 #- something that changes w/ activity periodically on step
    drawLine(x + 120, y, x + 120, y + thisSpecificLineLength, lineWidth = 8, fill='purple')
    
    # can be changed on step soon after receptorActive == True
    # last connector and segment pair, normal height
    drawLine(x + 116, y, x + 164 + app.connectorWidth, y, fill='purple', lineWidth=6)
    drawLine(x + 160, y, x + 160, y + segmentHeight, lineWidth = 8, fill='purple')
    if app.receptorActive:
        pass
        #draw new vertical line and new horizontal line connecting to the segment whose height is changing
        # drawLine(x + 156, y + segmentHeight, x + 204, y + segmentHeight, lineWidth = 8, fill='green')
   
def drawStartScreen(app):
    drawLabel("03-121 Final Project Animation", app.width/2, app.height/2 - 50, font='Arial', size=40, fill='black')
    drawLabel("Click to begin the animation!", app.width/2, app.height/2, font='Arial', size=40, fill='black')
    drawLabel("by Christopher Owad", app.width/2, app.height/2 + 50, font='Arial', size=40, fill='black')

def redrawAll(app):
    if not app.animationActive:
        drawStartScreen(app)
    else:
        if app.drawReceptorActive:
            drawRect(83, 70, 190, 240, fill = 'yellow', opacity = 50)
        drawOval(app.lx, app.ly, 16, 19, fill='yellow', border='black', borderWidth=2)
        for i in range(25):
            drawPhospholipid(app, 20 + i * 43,120, 1)
            drawPhospholipid(app, 20 + i * 43, 200, -1)
        drawTransmembraneReceptor(app, 100, 90)
        # drawPhospholipid(app, 20, 20)

def onMousePress(app, mouseX, mouseY):
    if not app.animationActive:
        app.animationActive = True

def moveLigand(app):
    if app.lx != 100:
        app.lx += 5
        app.ly = 2
    else:
        app.ly += 3
        if app.lx == 100 and 73 <= app.ly <= 77:
            app.ligandMoving = False
            app.drawReceptorActive = True
            app.receptorActive = True
def moveReceptor(app):
    app.connectorWidth += 5
    # app.newSegmentHeight 

def onStep(app):
    if app.animationActive:
        app.steps += 1
        if app.ligandMoving:
            moveLigand(app)
            # change values later
        if app.receptorActive:
            moveReceptor(app)
    
        # if app.steps % 14 == 0:
        #     app.drawReceptorActive = False
runApp()
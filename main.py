from cmu_graphics import *
def onAppStart(app):
    app.stepsPerSecond = 24
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
    app.thisSpecificLineLength = 150 * 1.4
    app.drawNewConnector = False
    app.newConnectorWidth = 0
    app.drawNewSegment = False
    app.newSegmentHeight = 0
    app.proteinActive = False
    app.pax = 500
    app.pay = 300
    app.pbx = 570
    app.pby = 300
    app.pgx = 615
    app.pgy = 300
    app.alphaActive = False
    app.gtp = False
    app.gdpx = 500
    app.gdpy = 300
    app.gtpx = -20
    app.gtpy = 300
    app.gameOver = False
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
    drawLine(x + 76, y + segmentHeight * 1.4, x + 84 + app.connectorWidth, y + segmentHeight * 1.4, lineWidth = 8, fill='purple')
    #here, draw the part after the changing part, that will not change despite activity
     #- something that changes w/ activity periodically on step
    drawLine(x + 120, y, x + 120, y + app.thisSpecificLineLength, lineWidth = 8, fill='purple')
    
    # can be changed on step soon after receptorActive == True
    # last connector and segment pair, normal height
    drawLine(x + 116, y, x + 164, y, fill='purple', lineWidth=6)
    drawLine(x + 160, y, x + 160, y + segmentHeight, lineWidth = 8, fill='purple')
    if app.receptorActive:
        if app.drawNewConnector:
            drawLine(x + 116, 252, x + 164 + app.newConnectorWidth, 252, lineWidth = 8, fill='purple')
        if app.drawNewSegment:
            drawLine(x + 180, 252, x + 180, 252 + app.newSegmentHeight, lineWidth = 8, fill='purple')
            #drawLine(x + 156, y + segmentHeight, x + 204, y + segmentHeight, lineWidth = 8, fill='green')
        #draw new vertical line and new horizontal line connecting to the segment whose height is changing
        # drawLine(x + 156, y + segmentHeight, x + 204, y + segmentHeight, lineWidth = 8, fill='green')
   
def drawStartScreen(app):
    drawLabel("03-121 Final Project Animation", app.width/2, app.height/2 - 50, font='Arial', size=40, fill='black')
    drawLabel("Click to begin the animation!", app.width/2, app.height/2, font='Arial', size=40, fill='black')
    drawLabel("by Christopher Owad", app.width/2, app.height/2 + 50, font='Arial', size=40, fill='black')

def redrawAll(app):
    if app.gameOver:
        drawLabel("Animation over!", app.width/2, app.height/2, font='Arial', size=40, fill='black')
        drawLabel("Thanks for watching!", app.width/2, app.height/2 + 50, font='Arial', size=40, fill='black')
        return
    if not app.animationActive:
        drawStartScreen(app)
    else:
        
        if app.drawReceptorActive:
            # draw highlight
            drawRect(83, 70, 210, 250, fill = 'yellow', opacity = 50)
        drawOval(app.lx, app.ly, 16, 19, fill='yellow', border='black', borderWidth=2)
        for i in range(25):
            drawPhospholipid(app, 20 + i * 43,120, 1)
            drawPhospholipid(app, 20 + i * 43, 200, -1)
        drawTransmembraneReceptor(app, 100, 90)
        if app.proteinActive:
            drawProtein(app)
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

def drawProtein(app):
    if app.alphaActive: border = 'yellow'
    else: border = None
    drawCircle(app.pax, app.pay, 40, fill='violet', border = border, borderWidth=5)
    drawLabel("α", app.pax, app.pay, font='Arial', size=30, fill='black')
    drawRect(app.gdpx, app.gdpy + 20, 30, 15, fill='white', align = 'center')
    drawLabel("GDP", app.gdpx, app.gdpy + 20, font='Arial', size=10, fill='black')
    drawRect(app.gtpx, app.gtpy + 20, 30, 15, fill='white', align = 'center')
    drawLabel("GTP", app.gtpx, app.gtpy + 20, font='Arial', size=10, fill='black')
    drawCircle(app.pbx, app.pby, 35, fill='blue')
    drawLabel("β", app.pbx, app.pby, font='Arial', size=20, fill='black')
    drawOval(app.pgx, app.pgy, 20, 45, fill='red')
    drawLabel("γ", app.pgx, app.pgy, font='Arial', size=20, fill='black')

def moveReceptor(app):
    if app.connectorWidth != 100:
        app.connectorWidth += 2
    if app.thisSpecificLineLength != 162:
        app.thisSpecificLineLength -= 8
    else:
        app.drawNewConnector = True
    if app.drawNewConnector:
        if not app.newConnectorWidth == 20:
            app.newConnectorWidth += 5
        else:
            app.drawNewSegment = True
    if app.drawNewSegment:
        if app.newSegmentHeight != 48:
            app.newSegmentHeight += 4
        else:
            app.proteinActive = True

def moveProtein(app):
    if app.pax > 290:
        app.pax -= 2
        app.pbx -= 2
        app.pgx -= 2
        app.gdpx -=2
    else:
        app.alphaActive = True

def moveGDP(app):
    if not app.gtp:
        app.gdpy += 5
        app.gtpx += 5
        if app.gtpx == app.pax:
            app.gtp = True

def moveAlpha(app):
    app.pax += 4
    app.pay += 3
    app.gtpx = app.pax
    app.gtpy = app.pay + 10
    if app.pay - 100 >= app.height:
        app.gameOver = True
    # app.gtpy += 3
def onStep(app):
    if app.animationActive:
        if app.alphaActive and app.gtp:
            moveAlpha(app)
        elif app.alphaActive and not app.gtp:
            moveGDP(app)
        if app.proteinActive:
            moveProtein(app)
        if app.receptorActive:
            moveReceptor(app)
        
        elif app.ligandMoving:
            moveLigand(app)
        app.steps += 1
        
runApp()
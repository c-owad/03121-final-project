from cmu_graphics import *
def onAppStart(app):
    app.stepsPerSecond = 5
    app.height = 600
    app.width = 800
    app.receptorActive = True
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
    #later, if app.receptorActive, we will make the ligand highlight yellow
    #these draw the head
    drawLine(x - width/3, y - height/2, x - width/3, y, fill='purple', lineWidth=6)
    drawLine(x + width/3, y - height/2, x + width/3, y, fill='purple', lineWidth=6)
    #draw connecting line between those, to finish the part that takes the ligand
    drawLine(x - width/3 - 3, y, x + width/3 + 3, y, fill='purple', lineWidth=6)
    # draw segments of receptor, in the forms of lines
    drawLine(x, y, x, y + segmentHeight, lineWidth = 8, fill='purple')
    #draw connecter to next segment, moving right
    drawLine(x - 4, y + segmentHeight, x + 44, y + segmentHeight, fill='purple', lineWidth=6)
    #draw next segment, vertically
    drawLine(x + 40, y, x + 40, y + segmentHeight, lineWidth = 8, fill='purple')
    #next connector
    drawLine(x + 36, y, x + 84, y, fill='purple', lineWidth=6)
    #new segment, veritcally, and extra long.
    drawLine(x + 80, y, x + 80, y + segmentHeight * 1.4, lineWidth = 8, fill='purple')
    #now: we draw the part that moves later, which will still be a series of lines, but have app variables stored that 
    drawLine(x + 76, y + segmentHeight * 1.4, x + 124, y + segmentHeight * 1.4, lineWidth = 8, fill='purple')
    #here, draw the part after the changing part, that will not change despite activity
    thisSpecificLineLength = segmentHeight * 1.4 #- something that changes w/ activity periodically on step
    drawLine(x + 120, y, x + 120, y + thisSpecificLineLength, lineWidth = 8, fill='purple')
    
    # can be changed on step soon after receptorActive == True
    # last connector and segment pair, normal height
    drawLine(x + 120, y, x + 160, y, fill='purple', lineWidth=6)
    drawLine(x + 156, y, x + 164,y + segmentHeight, lineWidth = 8, fill='purple')
    # drawLine(x + 160, y + thisSpecificLineLength, x + 160, y, lineWidth = 8, fill='purple')
    # for i in range(numSegments):
    #     if i % 2 == 0:
    #         # Upward arc
    #         drawArc(x, y - segmentHeight, segmentWidth, 2 * segmentHeight, 0, 180, fill=None, border='blue', borderWidth=3)
    #     else:
    #         # Downward arc
    #         drawArc(x, y, segmentWidth, 2 * segmentHeight, 180, 180, fill=None, border='blue', borderWidth=3)
    #     x += segmentWidth  # Move to the next segment

    # # Draw the receptor head at the top
    # drawCircle(x - segmentWidth / 2, y - segmentHeight, 15, fill='purple')
    # drawPolygon(x - width/2, y - height/2, x - width/2, y, x + width/2, y, x + width/2, y - height/2, fill=None, border='purple', borderWidth=6)
def redrawAll(app):
    for i in range(25):
        drawPhospholipid(app, 20 + i * 43,120, 1)
        drawPhospholipid(app, 20 + i * 43, 200, -1)
    drawTransmembraneReceptor(app, 100, 90)
    # drawPhospholipid(app, 20, 20)

# def onStep(app):

runApp()
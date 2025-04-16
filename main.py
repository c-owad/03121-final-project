from cmu_graphics import *
def onAppStart(app):
    app.stepsPerSecond = 5
    app.height = 600
    app.width = 800
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
    # drawPolygon(x - width/2, y - height/2, x - width/2, y, x + width/2, y, x + width/2, y - height/2, fill=None, border='purple', borderWidth=6)
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

def redrawAll(app):
    for i in range(25):
        drawPhospholipid(app, 20 + i * 43,120, 1)
        drawPhospholipid(app, 20 + i * 43, 200, -1)
    drawTransmembraneReceptor(app, 100, 90)
    # drawPhospholipid(app, 20, 20)

# def onStep(app):

runApp()
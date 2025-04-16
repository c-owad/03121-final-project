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

def drawTransmembraneReceptor(app, startX, startY, segmentWidth, segmentHeight, numSegments):
    x = startX
    y = startY
    drawArc(x, y, 30, 30, 180, 90, fill = 'white', border = 'black', borderWidth = 4)
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
    drawTransmembraneReceptor(app, 20, 100, 20, 50, 3)
    # drawPhospholipid(app, 20, 20)

# def onStep(app):

runApp()
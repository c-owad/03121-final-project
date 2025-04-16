from cmu_graphics import *
def onAppStart(app):
    app.stepsPerSecond = 5
    app.height = 600
    app.width = 800
def drawPhospholipid(app, cx, cy, orientation):
    r = 20
    #Draw the two tails of the phospholipid:
    drawLine(cx - r/2, cy, cx - r/2, cy + 50, fill='gray', lineWidth=3)
    drawLine(cx + r/2, cy, cx + r/2, cy + 50, fill='gray',lineWidth=3)
    #Draw the head of the phospholipid:
    drawCircle(cx, cy, r, fill='gray')
def redrawAll(app):
    for i in range(25):
        drawPhospholipid(app, 20 + i * 43,120)
    # drawPhospholipid(app, 20, 20)

runApp()
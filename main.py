from graphics import *

def main():
    a = 3.5
    b = color_rgb(0,0,0)

    win=GraphWin("CSE 342", 700, 700)
    win.setBackground(color_rgb(255,255,255))

    img = Image(Point(120, 90), "i.png")
    img.draw(win)

    lm = Line(Point(120, 600), Point(550, 600))
    lm.setWidth(3.5)
    lm.setOutline(color_rgb(0, 0, 0))
    lm.draw(win)

    lm1 = Line(Point(550,600),Point(550,250))
    lm1.setWidth(a)
    lm1.setOutline(b)
    lm1.draw(win)

    lm2 = Line(Point(550,250),Point(120, 250))
    lm2.setWidth(a)
    lm2.setOutline(b)
    lm2.draw(win)

    lm3 = Line(Point(120, 250), Point(120, 600))
    lm3.setWidth(a)
    lm3.setOutline(b)
    lm3.draw(win)

    lm3 = Line(Point(120, 250), Point(335,50))
    lm3.setWidth(a)
    lm3.setOutline(b)
    lm3.draw(win)

    lm3 = Line(Point(335, 50), Point(550,250))
    lm3.setWidth(a)
    lm3.setOutline(b)
    lm3.draw(win)

    door1 = Line(Point(275,600),Point(275,450))
    door1.setWidth(a)
    door1.setOutline(b)
    door1.draw(win)

    door1 = Line(Point(400, 600), Point(400, 450))
    door1.setWidth(a)
    door1.setOutline(b)
    door1.draw(win)

    door1 = Line(Point(275, 450), Point(400, 450))
    door1.setWidth(a)
    door1.setOutline(b)
    door1.draw(win)



    win.getMouse()
    win.close()


main()
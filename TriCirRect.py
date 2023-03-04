from graphics import *


def main():
    win = GraphWin("CSE 342", 700, 700)
    win.setBackground(color_rgb(255, 255, 255))
    a = 3
    b = "black"

    tri = Polygon(Point(350, 100), Point(550, 250), Point(150, 250))
    tri.setWidth(a)
    tri.setOutline(b)
    tri.setFill("orange")
    tri.draw(win)

    rect = Rectangle(Point(150, 250), Point(550, 600))

    # set some properties of the rectangle
    rect.setFill("blue")
    rect.setOutline(b)
    rect.setWidth(a)
    rect.draw(win)

    door = Rectangle(Point(300, 450), Point(400, 600))
    door.setFill("black")
    door.setOutline(b)
    door.setWidth(a)
    door.draw(win)

    window = Rectangle(Point(200, 300), Point(250, 350))
    window.setFill("black")
    window.setOutline(b)
    window.setWidth(a)
    window.draw(win)

    circle = Circle(Point(450, 320), 40)
    circle.setWidth(3)
    circle.setOutline("yellow")
    circle.setFill("red")
    circle.draw(win)

    img = Image(Point(200,200),"i.png")

    img.draw(win)


    win.getMouse()
    win.close()


main()

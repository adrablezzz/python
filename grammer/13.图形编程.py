# import graphics
# win = graphics.GraphWin()

from graphics import *

def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()

# main()

def get_click():
    win = GraphWin('getClick', 200, 200)
    p = win.getMouse()
    print('you click here:{},{}'.format(p.getX(), p.getY()))

# get_click()

def draw_tri():
    win = GraphWin('三角形')
    win.setCoords(0, 0, 10, 10)
    message = Text(Point(5, .5), 'click 3 points')
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    tri = Polygon(p1, p2, p3)
    tri.setFill('peachpuff')
    tri.setOutline('cyan')
    tri.draw(win)

    message.setText('点击任意关闭')
    win.getMouse()

draw_tri()
import turtle
import time

from numpy import true_divide 

class Draw:
    def __init__(self):
        turtle.pensize(5)
        turtle.pencolor('black')
        turtle.color('red')
        turtle.speed(3)
    
    def Drawing(self):
        for _ in range(5):
            turtle.left(144)
            turtle.forward(200)
    
    def Style(self):
        turtle.penup()
        turtle.goto(-270, -120)
        turtle.write("Slipknot", font=('Arial', 40, 'normal'))
        time.sleep(4)
if __name__ == "__main__":
    vini = Draw()
    vini.Drawing()
    vini.Style()

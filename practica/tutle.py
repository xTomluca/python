from tkinter import mainloop
import turtle
turtle.getscreen()
turtle.shape("turtle")    
turtle.shapesize(2,2,2)
turtle.color("red", "yellow")

turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.end_fill()



mainloop()

# turtle.forward() Se mueve hacia adelante
# turtle.backward() Se mueve hacia atras
# turtle.left() Angulos hacia la izquierda
# turtle.right() Angulo hacia la derecha
# turtle.fillcolor("green")


"""
Example to demonstrate the process for designing functions using the turtle module. Draw a triangle here.
"""
import turtle
import math

bob = turtle.Turtle()
print(bob)

# Move the turtle forward
bob.fd(300)

# Turn the turtle left of angle 90 degrees
bob.lt(90)

# Move the turtle forward
bob.fd(300)

# Move the turtle left of angle 135 degrees
bob.lt(135)

# Move the turtle forward
bob.fd(300 * math.sqrt(2))

# Tell the window to wait for the user to do something.
turtle.mainloop()

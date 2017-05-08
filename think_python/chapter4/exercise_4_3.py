"""
Exercise 4.3 to use TurtleWorld.
Draw different shapes.
"""

import turtle
import math

def draw(t, n, length, turn):
	"""
	Take a turtle and draw based on the number of
	lines, the length of the line and the angle
	between lines.
	"""
	for x in xrange(0, n):
		t.lt(turn)
		t.fd(length)

def square(t, length):
	"""
	Take a turtle and draw a rectangle. 
	Each side has length of "length".
	"""
	polygon(t, length, 4)

def polygon(t, length, n):
	"""
	Take a turtle and draw a n-sided regular polygon.
	"""
	turn = float(360) / n
	draw(t, n, length, turn) 

def circle(t, r):
	"""
	Take a turtle and draw a circle with radius r
	through calling polygon.
	"""
	arc(t, r, 360)

def arc(t, r, angle):
	"""
	Draw a fraction of the circle.
	"""
	circumference = 2 * math.pi * r * angle / 360.0
	n = 100
	length = circumference / n
	turn = float(angle) / n
	draw(t, n, length, turn)

def main():
	bob = turtle.Turtle()
	arc(bob, 50, 270)
	turtle.mainloop()

main()


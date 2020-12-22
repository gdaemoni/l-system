import turtle
import copy
import time

FORWARD = 5
RIGHT = 90
LEFT = 90
SPEED = 50

axiom = {
	'koch': 'F+F+F+F',
}

def init(name = "turtle", speed = SPEED, shapesize = [3, 3, 3], pensize = 3):
	turtle.shape(name)
	turtle.shapesize(*shapesize)
	turtle.pensize(2)
	turtle.speed(speed)
	turtle.hideturtle()
	turtle.color('white')
	# turtle.goto(-400, 400)
	turtle.color('black')
	return turtle

def draw_curve(turtle, curve):
	for ch in curve:
		if ch == 'F':
			turtle.forward(FORWARD)
		elif ch == '+':
			turtle.right(RIGHT)
		elif ch == '-':
			turtle.left(LEFT)
	turtle.update()

def generate_string(axiom, string, size=1):
	if string != '':
		axiom = copy.copy(string)
	if size == 0:
		return string
	for ch in axiom:
		if ch == '+':
			string += '+'
		elif ch == '-':
			string += '-'
		elif ch == 'F':
			string += "F+F-F-F+F"
	size -= 1
	axiom = ''
	return generate_string(axiom, string, size)

def main():
	turtle = init()
	curve = generate_string(axiom['koch'], "", 4)
	print(curve)
	for _ in range(3):
		draw_curve(turtle, curve)
	time.sleep(60)

if __name__ == "__main__":
	main()
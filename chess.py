import turtle
import screen
#Tobie Rathbun, thiSpaghetti, 2021

#define turtles
piece = turtle.Turtle()
gameboard = turtle.Turtle()
turtle.tracer(0,0)


#define variables
#rotation
turn = 90
spin = 180

#metrics
unit = 3
two = unit * 2
three = unit * 3
four = unit * 4
sev = unit * 7
elev = unit * 11

#drawing
fill = "white"
pen = "black"

#gameboard
tileSize = 25 * unit
halfSide = round(tileSize / 2) #round here fixes aliasing
topX = -300
topY = 300 
rowVar = 0
colVar = 0

#gamegrid
rowForw = halfSide + tileSize * rowVar
colDown = halfSide + tileSize * colVar
pieceX = topX + rowForw
pieceY = topY - elev - colDown 


#define draw speed
piece.speed(0)
gameboard.speed(0)

#define drawing tools
piece.hideturtle()
gameboard.hideturtle()


piece.fillcolor(fill)
piece.pencolor(pen)

#define fucntions

#gameboard
def blackSquare():
	gameboard.begin_fill()
	for i in range(4):
		gameboard.forward(tileSize)
		gameboard.right(turn)
	gameboard.end_fill()
	
def topLeft():
	gameboard.up()			#stops pen
	gameboard.setposition(topX,topY)	#goes 0,0
	gameboard.down() 		#starts pen

def makeBoard():
	x = 0
	for i in range(4):
		topLeft()					#orients top left
		
		if x > 1:
			gameboard.right(turn)		#faces south
			gameboard.forward(tileSize * x)#next row
			gameboard.left(turn)		#faces east
		
		gameboard.forward(tileSize)		#moves to second column

		for i in range(3):			#white row
			blackSquare()
			gameboard.forward(tileSize * 2)

		blackSquare()
		
		x = x + 1
		
		topLeft()
		gameboard.right(turn)			#faces south
		gameboard.forward(tileSize * x)	#moves south to the next row
		gameboard.left(turn)			#faces east

		for i in range(4):			#black row
			blackSquare()
			gameboard.forward(tileSize * 2)

		x = x + 1
		
		gameboard.right(turn)			#faces south
		gameboard.forward(tileSize)		#draws last square
		gameboard.left(turn)			#faces east
		
		if x > 7:
			gameboard.backward(tileSize * 8)
	

#drawing colors
def white():				#makes a white piece
	global fill
	global pen
	fill = "white"
	pen = "black"
	piece.fillcolor(fill)
	piece.pencolor(pen)
	
def black():				#makes a black piece
	global fill
	global pen
	fill = "black"
	pen = "white"
	piece.fillcolor(fill)
	piece.pencolor(pen)

#gamegrid
def newGrid():
	global pieceX
	global pieceY
	global rowVar
	global colVar
	rowForw = halfSide + tileSize * rowVar
	colDown = halfSide + tileSize * colVar
	pieceX = topX + rowForw
	pieceY = topY - colDown - elev


#shapes
	
def bumpR():
	piece.circle(unit,spin)		#semicircle, faces west
	piece.forward(unit)			#moves west
	piece.right(spin)			#faces east for semicircle
	
def bumpL():
	piece.circle(-unit,spin)	#semicircle, faces west
	piece.forward(unit)			#moves west
	piece.right(spin)			#faces east for semicircle

def startDraw():
	piece.up()
	piece.setposition(topX,topY)#goes to 0,0
	piece.down()
	piece.begin_fill()

def halfway():
	piece.up()					#lifts pen
	piece.setposition(pieceX,pieceY)	#goes to x,y
	piece.down()				#activates pen
	piece.begin_fill()

def rightBase():
	piece.forward(sev)			#moves east
	for i in range(3):			#makes 3 northward bumps 
		bumpR()
		
def leftBase():
	piece.forward(sev)			#moves west
	for i in range(3):			#makes 3 northward bumps 
		bumpL()		
		
		
#pieces		
		
def rook():
	halfway()
	rightBase()

	#rook right 
	piece.circle(two, -turn)	#draws quarter circle to the north facing south
	piece.right(spin)			#faces north
	piece.forward(sev)			#moves north
	piece.right(turn)			#faces right
	piece.circle(three, turn)	#semicircle facing north
	piece.forward(four)			#moves north
	piece.left(turn)			#faces west
	piece.forward(two)			#moves west
	piece.left(turn)			#faces south
	piece.forward(two)			#moves south
	piece.right(turn)			#face west
	piece.forward(two)			#moves west
	piece.right(turn)			#faces north
	piece.forward(two)			#moves north
	piece.left(turn)			#faces west
	piece.forward(two)			#moves west
	piece.end_fill()

	halfway()
	leftBase()


	#rook left
	piece.circle(-two,-turn)
	piece.right(spin)
	piece.forward(sev)			#moves north
	piece.left(turn)			#faces west

	piece.circle(-three,turn)
	piece.forward(four)
	piece.left(-turn)			#faces west
	piece.forward(two)			#moves west
	piece.left(-turn)			#faces south
	piece.forward(two)			#moves south
	piece.right(-turn)			#face west
	piece.forward(two)		#moves west
	piece.right(-turn)	#faces north
	piece.forward(two)		#moves north
	piece.left(-turn)		#faces west
	piece.forward(two)		#moves west
	piece.end_fill()
	piece.hideturtle()
	
def pawn():
	halfway()
	rightBase()

	#pawn right 
	piece.circle(two, -turn)		#draws quarter circle to the north facing south
	piece.right(spin)			#faces north
	piece.forward(four)		#moves north
	piece.right(turn)			#faces right
	piece.circle(two, spin)		#semicircle facing west
	piece.forward(four)		#moves west
	piece.end_fill()


	halfway()
	leftBase()


	#pawn left
	piece.circle(-two,-turn)
	piece.right(spin)
	piece.forward(four)
	piece.right(turn)
	piece.circle(two,-spin)
	piece.right(spin)
	piece.forward(two)
	piece.end_fill()
	piece.hideturtle()	
	

makeBoard()




rowVar = 3
colVar = 3
newGrid()
black()
pawn()
turtle.update()

def dRight():
	global rowVar
	piece.reset()
	if rowVar < 7:
		rowVar = rowVar + 1
	newGrid()
	white()
	rook()
	turtle.update()
	
def dLeft():
	global rowVar
	piece.reset()
	if rowVar > 0:
		rowVar = rowVar - 1
	newGrid()
	white()
	rook()
	turtle.update()
	
def dDown():
	global colVar
	piece.reset()
	if colVar < 7:
		colVar = colVar + 1
	newGrid()
	white()
	rook()
	turtle.update()
	
def dUp():
	global colVar
	piece.reset()
	if colVar > 0:
		colVar = colVar - 1
	newGrid()
	white()
	rook()
	turtle.update()
	
window = turtle.Screen()
turtle.onkey(dLeft, "Left")
turtle.onkey(dRight, "Right")
turtle.onkey(dDown, "Down")
turtle.onkey(dUp, "Up")

turtle.listen()

turtle.done()

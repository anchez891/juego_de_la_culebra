import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0


#Ventana
frame = turtle.Screen()
frame.title("Juego de Pong")
frame.bgcolor("black")
frame.setup(width = 600, height = 600)
frame.tracer(0)

#Cabeza de la serpiente
Cabeza = turtle.Turtle()
Cabeza.speed(0)
Cabeza.shape("square")
Cabeza.color("white")
Cabeza.penup()
Cabeza.goto(0, 0)
Cabeza.direccion = "Stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0, 100)

#Texo
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0	High Score: 0", align = "center", font = ("Courier", 24, "normal" ))

#Segmentos / cuerpo serpiente
segmentos = []

#Funciones
def arriba():
	Cabeza.direccion = "up"


def abajo():
	Cabeza.direccion = "down"


def izquierda():
	Cabeza.direccion = "left"



def derecha():
	Cabeza.direccion = "right"

#funcion del movimiento
def mov():
	if Cabeza.direccion == "up":
		y = Cabeza.ycor()
		Cabeza.sety(y + 20)

	elif Cabeza.direccion == "down":
		y = Cabeza.ycor()
		Cabeza.sety(y - 20)

	elif Cabeza.direccion == "left":
		x = Cabeza.xcor()
		Cabeza.setx(x - 20)

	elif Cabeza.direccion == "right":
		x = Cabeza.xcor()
		Cabeza.setx(x + 20)

#Teclado
frame.listen()
frame.onkeypress(arriba, "Up")
frame.onkeypress(abajo, "Down")
frame.onkeypress(izquierda, "Left")
frame.onkeypress(derecha, "Right")

while True:
	frame.update()

	#colisiones bordes
	if Cabeza.xcor() > 280 or Cabeza.xcor() < -280 or Cabeza.ycor() > 280 or Cabeza.ycor() < -280:
		time.sleep(1)
		Cabeza.goto(0,0)
		Cabeza.direccion = "Stop"

		#Esconder segmentos
		for segmento in segmentos:
			segmento.goto(1000,1000)

		#limpiar lista de segmentos
		segmentos.clear()

		#resetear el marcador
		score = 0
		texto.clear()
		texto.write("Score: {}	High Score: {}".format(score, high_score),
		 		align = "center", font = ("Courier", 24, "normal" ))

		#resetear el marcador
		score = 0
		texto.clear()
		texto.write("Score: {}	High Score: {}".format(score, high_score),
		 align = "center", font = ("Courier", 24, "normal" ))


	#colisiones de comida
	if Cabeza.distance(comida) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)

		#Aumentar marcador
		score += 10

		if score > high_score:
			high_score = score

		texto.clear()
		texto.write("Score: {}	High Score: {}".format(score, high_score),
		 align = "center", font = ("Courier", 24, "normal" ))

	#mover el cuerpo de la serpiente
	totalSeg = len(segmentos)
	for index in range(totalSeg -1 , 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)

	if totalSeg > 0:
		x = Cabeza.xcor()
		y = Cabeza.ycor()
		segmentos[0].goto(x,y)

		

	mov()

	#colisiones cuerpo
	for segmento in segmentos:
		if segmento.distance(Cabeza) < 20:
			time.sleep(1)
			Cabeza.goto(0,0)
			Cabeza.direccion = "Stop"

			#Esconder segmentos
			for segmento in segmentos:
				segmento.goto(1000,1000)

			#limpiar lista de segmentos
			segmentos.clear()

			#resetear el marcador
			score = 0
			texto.clear()
			texto.write("Score: {}	High Score: {}".format(score, high_score),
		 		align = "center", font = ("Courier", 24, "normal" ))




	time.sleep(posponer)
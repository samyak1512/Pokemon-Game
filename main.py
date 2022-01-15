import turtle
from Pen import CharacterPen
import math
import random


userpokemon = ''

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH +220, SCREEN_HEIGHT+20)
wn.title("Pokemon")
wn.bgcolor("White")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

character_pen = CharacterPen("Blue", 1.0)
character_pen.draw_string(pen, "Pokemon", 0, 160)

character_pen.draw_string(pen, "Choose a starter Pokemon", 0, 50)

wn.register_shape("charmander.gif")

charmander = turtle.Turtle()
charmander.shape('charmander.gif')
charmander.speed(0)
charmander.penup()
charmander.goto(-250,-150)

character_pen.draw_string(pen, 'Charmander - A', -250,-250)

wn.register_shape("squirtle.gif")

squirtle = turtle.Turtle()
squirtle.shape('squirtle.gif')
squirtle.speed(0)
squirtle.penup()
squirtle.goto(0,-150)

character_pen.draw_string(pen, 'Squirtle - B', 0,-250)

wn.register_shape("bulbasaur.gif")

bulbasaur = turtle.Turtle()
bulbasaur.shape('bulbasaur.gif')
bulbasaur.speed(0)
bulbasaur.penup()
bulbasaur.goto(250,-150)

character_pen.draw_string(pen, 'Bulbasaur - C', 250,-250)


def charmander():
    global userpokemon
    userpokemon = 'Charmander'
def bulbasaur():
    global userpokemon
    userpokemon = 'Bulbasaur'
def squirtle():
    global userpokemon
    userpokemon = 'Squirtle'

wn.listen()
wn.onkeypress(charmander,'a')
wn.onkeypress(squirtle,'b')
wn.onkeypress(bulbasaur,'c')


while True:
   # character_pen.
    character_pen.draw_string(pen,f'Your Starter Pokemon: {userpokemon}', -300,250)




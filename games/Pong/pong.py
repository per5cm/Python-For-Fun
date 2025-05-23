# Simple Pong game.

import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong by per5cm")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score.
score_a = 0
score_b = 0

# Sound.

def play_sound():
    winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

# Paddle A.
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B.
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball.
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8     #ball d stands for delta/change and its coords x,y how fast ball is moving on the screen.
ball.dy = -0.8

# Pen.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function.
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding.
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

# Main game loop.
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    time.sleep(0.01)
    
    # Move the ball.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking top and bottom.
    if ball.ycor() > 290 or ball.ycor() < - 290:
        ball.dy *= -1
        play_sound()
    
    # Border checking left and right.
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= 1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= 1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        
    # Paddle and ball collisions.
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.dx > 0 and 
        paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1  # Reverse X direction
        play_sound()

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.dx < 0 and 
        paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1  # Reverse X direction
        play_sound()  
        

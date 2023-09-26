import turtle

wn = turtle.Screen()
wn.title("Pong by Me")
wn.bgcolor("black")
wn.setup(width=1200, height=800)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Player A Paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=7, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-550, 0)

paddle_a_top = turtle.Turtle()
paddle_a_top.speed(0)
paddle_a_top.shape("square")
paddle_a_top.color("red")
paddle_a_top.shapesize(stretch_wid=1, stretch_len=7)
paddle_a_top.penup()
paddle_a_top.goto(0, 350)

# Player B Paddles
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup()
paddle_b.goto(550, 0)

paddle_b_bot = turtle.Turtle()
paddle_b_bot.speed(0)
paddle_b_bot.shape("square")
paddle_b_bot.color("blue")
paddle_b_bot.shapesize(stretch_wid=1, stretch_len=7)
paddle_b_bot.penup()
paddle_b_bot.goto(0, -350)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write(f"Player A: 0  Player B: 0", align="center", font=('Courier', 24, "bold"))



# Player A movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60
    paddle_a.sety(y)

def paddle_a_right():
    x = paddle_a_top.xcor()
    x += 60
    paddle_a_top.setx(x)

def paddle_a_left():
    x = paddle_a_top.xcor()
    x -= 60
    paddle_a_top.setx(x)

# Keybinds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.listen()
wn.onkeypress(paddle_a_down, "s")
wn.listen()
wn.onkeypress(paddle_a_right, "d")
wn.listen()
wn.onkeypress(paddle_a_left, "a")

# Player B Movement Functions

def paddle_b_up():
    y = paddle_b.ycor()
    y += 60
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60
    paddle_b.sety(y)

def paddle_b_right():
    x = paddle_b_bot.xcor()
    x += 60
    paddle_b_bot.setx(x)

def paddle_b_left():
    x = paddle_b_bot.xcor()
    x -= 60
    paddle_b_bot.setx(x)

# Keybinds
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.listen()
wn.onkeypress(paddle_b_down, "Down")
wn.listen()
wn.onkeypress(paddle_b_right, "Right")
wn.listen()
wn.onkeypress(paddle_b_left, "Left")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    # Paddle Bouncing
    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *=-1
        ball.dy *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=('Courier', 24, "bold"))

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *=-1
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=('Courier', 24, "bold"))

    if ball.ycor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        ball.dy *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=('Courier', 24, "bold"))
    
    if ball.ycor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        ball.dy *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=('Courier', 24, "bold"))

    # Blue Paddle Bounces
    if (ball.xcor() > 540 and ball.xcor() < 550) and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70):
        ball.dx *= -1

    if (ball.ycor() > paddle_b_bot.ycor() - 10 and ball.ycor() < paddle_b_bot.ycor() + 10) and (ball.xcor() > paddle_b_bot.xcor() - 70 and ball.xcor() < paddle_b_bot.xcor() + 70):
        ball.dy *= -1

    # Red Paddle Bounces
    if (ball.xcor() < -540 and ball.xcor() > -550) and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70):
        ball.dx *= -1

    if (ball.ycor() > paddle_a_top.ycor() - 10 and ball.ycor() < paddle_a_top.ycor() + 10) and (ball.xcor() > paddle_a_top.xcor() - 70 and ball.xcor() < paddle_a_top.xcor() + 70):
        ball.dy *= -1

    # # Victory
    # if score_a == 11:
    #     victory = turtle.Turtle()
    #     victory.speed(0)
    #     victory.color("green")
    #     victory.penup()
    #     victory.hideturtle()
    #     victory.goto(0, 0)
    #     victory.write(f"Congratulations player A WINS!!!", align="center", font=('Courier', 24, "bold"))
        
    
    # elif score_b == 11:
    #     victory = turtle.Turtle()
    #     victory.speed(0)
    #     victory.color("green")
    #     victory.penup()
    #     victory.hideturtle()
    #     victory.goto(0, 0)
    #     victory.write(f"Congratulations player B WINS!!!", align="center", font=('Courier', 24, "bold"))
            

    
            
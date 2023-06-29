from turtle import *
import random

#vorbereitung-------------------------------------------------------------------

#Variablen
spielaktiv = True
pL = 0
pR = 0
xspeed = 4
yspeed = random.randint(2, 4)
zufallx = random.randint(1, 2)
zufally = random.randint(1, 2)
ballstarty=0
ballstartx=0
timer1 = 0
abfrage = int(input("Für Übungsbereich 1 drücken, für Mehrspieler 2 drücken: "))
sppunkte = 0
a = 1

xspeicher = xspeed
yspeicher = yspeed

if zufallx == 2:
    xspeed = -xspeed
if zufally == 2:
    yspeed = -yspeed

# Funktionen
def hochL():
    SpielerL.fd(35)
    
def runterL():
    SpielerL.bk(35)
    
def hochR():
    SpielerR.fd(35)
    
def runterR():
    SpielerR.bk(35)
    
#def pause1():
#    global a
#    a = -a
#    print('pause on / off')
    
# set screen size
sc = Screen()


# Set up game screen
sc.setup(1200, 625)
sc.bgcolor("black")

#turtles------------------------------------------------------------------------

#test
#test = Turtle()
#test.setx(-500)
#test.color("white")
##test.goto(-500, 70)
#test.seth(90)
#test.bk(140)

#ausgabe
ausgabe = Turtle()
ausgabe.up()
ausgabe.hideturtle()
ausgabe.color("white")
ausgabe.goto(-300, 0)

#MittelLinie
Mittellinie = Turtle()
Mittellinie.up()
Mittellinie.shape("square")
Mittellinie.shapesize(stretch_wid=50, stretch_len=0.5)
Mittellinie.color('white')
Mittellinie.speed(0)

#spieler_links
SpielerL = Turtle()
SpielerL.up()
SpielerL.speed(0)
SpielerL.setx(-550)
SpielerL.shape("square")
SpielerL.shapesize(stretch_wid=1.5, stretch_len=7)
SpielerL.seth(90)
SpielerL.color("white")


#spieler_rechts
SpielerR = Turtle()
SpielerR.up()
SpielerR.speed(0)
SpielerR.setx(555)
SpielerR.shape("square")
SpielerR.shapesize(stretch_wid=1.5, stretch_len=7)
SpielerR.seth(90)
SpielerR.color("white")


#Ball
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.up()
ball.speed(0)

#PunkteLinks
punkteL = Turtle()
punkteL.speed(0)
punkteL.up()
punkteL.goto(-500, 200)
punkteL.hideturtle()
punkteL.color('white')

#PunkteRechts
punkteR = Turtle()
punkteR.speed(0)
punkteR.up()
punkteR.goto(450, 200)
punkteR.hideturtle()
punkteR.color('white')

#Spiel--------------------------------------------------------------------------

#Onkey
#Links
onkey(hochL, 's')
onkey(runterL, 'x')
#Rechts
onkey(hochR, 'Up')
onkey(runterR,'Down')

#onkey(pause1, 'e')
listen()


if abfrage == 2:
#Multiplayer--------------------------------------------------------------------
    print('preparing for multiplayer...')
    punkteL.write(pL, font=("Verdana", 65, "normal"))
    punkteR.write(pR, font=("Verdana", 65, "normal"))
    while spielaktiv:
        #listen()
        ballstartx = ballstartx + xspeed
        ballstarty = ballstarty + yspeed
        ball.setx(ballstartx)
        ball.sety(ballstarty)
        timer1 = timer1 + 1
    
        #BeschleunigungBall
        if timer1 % 600 == 0:
            if xspeed > 0:
                xspeed = xspeed + 1
            else:
                xspeed = xspeed - 1
            
#           if yspeed > 0:
#               yspeed = yspeed + 1
#           else:
#               yspeed = yspeed - 1
            
    
        if ball.xcor() >= 560 or ball.xcor() <= -565:
            if ball.xcor() >= 0:
                punkteL.color('black')
                punkteL.write(pL, font=("Verdana", 65, "normal"))
                pL = pL + 1
                punkteL.color('white')
                punkteL.write(pL, font=("Verdana", 65, "normal"))
            
            if ball.xcor() <= 0:
                punkteR.color('black')
                punkteR.write(pR, font=("Verdana", 65, "normal"))
                pR = pR + 1
                punkteR.color('white')
                punkteR.write(pR, font=("Verdana", 65, "normal"))
        
            #Punkteanzeige
            print('l', pL,'r', pR)
        
            ball.setx(0)
            ball.sety(0)
        
            ballstartx = 0
            ballstarty = 0
            xspeed = xspeicher
            yspeed = yspeicher
            
            if xspeed > 0:
                xspeed = -xspeed
        
            if pL == 5 or pR == 5:
                spielaktiv = False
                SpielerL.hideturtle
                SpielerR.hideturtle
                ball.hideturtle
                Mittellinie.hideturtle
            
        #Reflexion oben/unten
        if ball.ycor() >= 305 or ball.ycor() <= -295:
            yspeed = -yspeed
    
    
        #Reflexion
        #links
        if ball.xcor() <= SpielerL.xcor() + 17:
            #mitte
            if ball.ycor() > SpielerL.ycor() - 31 and ball.ycor() < SpielerL.ycor() + 31:
                xspeed = -xspeed
                ball.setx(ball.xcor() + 10)
            #oben
            if ball.ycor() > SpielerL.ycor() + 31 and ball.ycor() < SpielerL.ycor() +70:
                xspeed = -xspeed
                yspeed = yspeed + 2
                ball.setx(ball.xcor() + 10)
            #unten
            if ball.ycor() > SpielerL.ycor() -70 and ball.ycor() < SpielerL.ycor() -31:
                xspeed = -xspeed
                yspeed = yspeed - 2
                ball.setx(ball.xcor() + 10)
        #rechts
        if ball.xcor() >= SpielerR.xcor() - 17:
            #mitte
            if ball.ycor() > SpielerR.ycor() - 31 and ball.ycor() < SpielerR.ycor() + 31:
                xspeed = -xspeed
                ball.setx(ball.xcor() - 10)
            #oben
            if ball.ycor() > SpielerR.ycor() + 31 and ball.ycor() < SpielerR.ycor() +70:
                xspeed = -xspeed
                yspeed = yspeed + 2
                ball.setx(ball.xcor() - 10)
            #unten
            if ball.ycor() > SpielerR.ycor() -70 and ball.ycor() < SpielerR.ycor() -31:
                xspeed = -xspeed
                yspeed = yspeed - 2
                ball.setx(ball.xcor() - 10)
                
                
                
#singleplayer-------------------------------------------------------------------                
                
if abfrage == 1:
    print('preparing for player with no friends...')
    SpielerL.hideturtle()
    punkteL.setx(-400)
    punkteL.write(('Timer:'), font=("Verdana", 40, "normal"))
    punkteL.setx(-200)
    punkteR.setx(100)
    punkteR.write(('Gegentreffer:'), font=("Verdana", 40, "normal"))
    punkteR.setx(500)
    if ballstartx > 0:
        ballstart = -ballstart
    punkteR.write(0, font=("Verdana", 40, "normal"))
    while spielaktiv:
        #listen()
        ballstartx = ballstartx + xspeed
        ballstarty = ballstarty + yspeed
        ball.setx(ballstartx)
        ball.sety(ballstarty)
        timer1 = timer1 + 1
    
        #BeschleunigungBall
        if timer1 % 600 == 0:
            if xspeed > 0:
                xspeed = xspeed + 1
            else:
                xspeed = xspeed - 1
        if timer1 % 80 == 0:
            punkteL.color('black')
            punkteL.write(sppunkte, font=("Verdana", 40, "normal"))
            sppunkte = sppunkte + 1
            punkteL.color('white')
            punkteL.write(sppunkte, font=("Verdana", 40, "normal"))
            
#           if yspeed > 0:
#               yspeed = yspeed + 1
#           else:
#               yspeed = yspeed - 1
            
    
        if ball.xcor() >= 550:
            #Punkteanzeige
            punkteR.color('black')
            punkteR.write(pR, font=("Verdana", 40, "normal"))
            pR = pR + 1
            punkteR.color('white')
            punkteR.write(pR, font=("Verdana", 40, "normal"))
            
            ball.setx(0)
            ball.sety(0)
        
            ballstartx = 0
            ballstarty = 0
        
            xspeed = -xspeed
        #Reflexion oben/unten
        if ball.ycor() >= 305 or ball.ycor() <= -295:
            yspeed = -yspeed
    
    
        #Reflexion
        #links
        if ball.xcor() <= -600:
           xspeed = -xspeed
        #rechts
        if ball.xcor() >= SpielerR.xcor() - 17:
            #mitte
            if ball.ycor() > SpielerR.ycor() - 30 and ball.ycor() < SpielerR.ycor() + 30:
                xspeed = -xspeed
            #oben
            if ball.ycor() > SpielerR.ycor() + 31 and ball.ycor() < SpielerR.ycor() +70:
                xspeed = -xspeed
                yspeed = yspeed + 2
            #unten
            if ball.ycor() > SpielerR.ycor() -70 and ball.ycor() < SpielerR.ycor() -31:
                xspeed = -xspeed
                yspeed = random.randint(1, 3)
            speicher = timer1
         #PauseMenu
#        while a == -1:
#            onkey(pause1, 'e')
#            print(a)
else:
    print('Versuchs nochmal')
    
SpielerR.hideturtle()
SpielerL.hideturtle()
ball.hideturtle()
Mittellinie.hideturtle()
if pL > pR:
    ausgabe.write(("congrats left!"), font=("Verdana", 65, "normal"))
if pL < pR:
    ausgabe.write(("congrats right!"), font=("Verdana", 65, "normal"))
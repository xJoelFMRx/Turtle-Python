from turtle import *
from math import *

speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# Draw flower center
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# Define points to draw letters
def point(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(4), end_fill()

# Function to draw 'T'
def draw_T(x, y):
    positions_t = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30), (x+24, y+30),
                   (x+12, y+30), (x+12, y+24), (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y)]

    for pos in positions_t:
        point(*pos)

# Function to draw 'Ú'
def draw_U(x, y):
    positions_u = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x+3, y+3), (x+6, y), (x+12, y-1), (x+18, y), (x+21, y+3),
                   (x+24, y+6), (x+24, y+12), (x+24, y+18), (x+24, y+24), (x+24, y+30),
                   (x+12, y+36), (x+16, y+40)]

    for pos in positions_u:
        point(*pos)

# Function to draw 'M'
def draw_M(x, y):
    positions_m = [(x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30),
                   (x+6, y+24), (x+12, y+18),
                   (x+18, y+24), (x+24, y+30), (x+24, y+24), (x+24, y+18), (x+24, y+12), (x+24, y+6), (x+24, y)]
    for pos in positions_m:
        point(*pos)

# Function to draw 'B' 
def draw_B(x, y):
    positions_b = [(x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30),
                   (x+6, y+30), (x+12, y+30), (x+18, y+27),
                   (x+21, y+24), (x+21, y+21), (x+18, y+18),
                   (x+12, y+15), (x+18, y+12), (x+21, y+9),
                   (x+21, y+6), (x+18, y+3), (x+12, y), (x+6, y)]
    for pos in positions_b:
        point(*pos)

# Function to draw 'R' 
def draw_R(x, y):
    positions_r = [(x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30),
                   (x+6, y+30), (x+12, y+30), (x+18, y+27),
                   (x+21, y+24), (x+21, y+21), (x+18, y+18),
                   (x+12, y+15), (x+18, y+6), (x+24, y)]
    for pos in positions_r:
        point(*pos)

# Function to draw 'J'
def draw_J(x, y):
    positions_j = [(x+24, y+30), (x+24, y+24), (x+24, y+18), (x+24, y+12), (x+24, y+6),
                   (x+21, y+3), (x+18, y), (x+12, y-1), (x+6, y), (x+3, y+3),
                   (x, y+6)]
    for pos in positions_j:
        point(*pos)

# Function to draw 'A'
def draw_A(x, y):
    positions_a = [(x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30),
                   (x+6, y+30), (x+12, y+30), (x+18, y+30), (x+24, y+30),
                   (x+24, y+24), (x+24, y+18), (x+24, y+12), (x+24, y+6), (x+24, y),
                   (x, y+15), (x+6, y+15), (x+12, y+15), (x+18, y+15), (x+24, y+15)]
    for pos in positions_a:
        point(*pos)

# Function to draw 'Y'
def draw_Y(x, y):
    positions_y = [(x, y+30), (x+6, y+24), (x+12, y+18),
                   (x+18, y+24), (x+24, y+30),
                   (x+12, y+18), (x+12, y+12), (x+12, y+6), (x+12, y)]
    for pos in positions_y:
        point(*pos)
# Function to draw 'O'
def draw_O(x, y):
    positions_o = [(x, y+6), (x, y+12), (x, y+18), (x, y+24),
                   (x+6, y+30), (x+12, y+30), (x+18, y+30),
                   (x+24, y+24), (x+24, y+18), (x+24, y+12), (x+24, y+6),
                   (x+18, y), (x+12, y), (x+6, y)]
    for pos in positions_o:
        point(*pos)
# Function to draw 'U'
def draw_U(x, y):
    positions_u = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x+6, y), (x+12, y), (x+18, y),
                   (x+24, y+6), (x+24, y+12), (x+24, y+18), (x+24, y+24), (x+24, y+30)]
    for pos in positions_u:
        point(*pos)

# Draw 'YOU'
draw_Y(-42, -20)
draw_O(-12, -20)
draw_U(18, -20)

# Draw 'TÚ'
#draw_T(-27, -20)
#draw_U(7, -20)

# Draw 'MM'
#draw_M(-27, -20)
#draw_M(7, -20)

# Draw 'BR'
#draw_B(-27, -20)
#draw_R(7, -20)

# Draw 'JM'
#draw_J(-27, -20)
#draw_M(7, -20)

# Draw 'AM'
#draw_A(-27, -20)
#draw_M(7, -20)

# Draw 'MR'
#draw_M(-27, -20)
#draw_R(7, -20)

hideturtle()
done()
"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

#Se inician contadores de clicks y parejas
clicks= 0
parejas=0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    #Se cambio el color de tablero para que sea mas facil para el usuario ver las fichas
    #Se cambio a una paleta de colores que ayuda a la memoria de las personas incluyendo los colores de las fichas
    color('#f6caec', '#fffb9c')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    global clicks
    global parejas
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    # Cada que hay un tap es que hay un click mas
    clicks+=1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Se marca cuando se ha encontrado una pareja
        parejas+=1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        #Posicionamos las fichas dentro del cuadrado
        goto(x + 26, y+4)
        color('#473543')
        #Alineamos las fichas con ayuda de align="center"
        write(tiles[mark],align="center",font=('Arial', 30, 'normal'))
    
    # Se van desplegando la cantidad de clicks
    goto(0,210)
    write (clicks,font=("Arial",20))

    # Si se encuentran todas las parejas te dice que lo has logrado
    if parejas == 32: 
        up()
        goto(0, 0)
        color('#f0cc35')
        write("YA SE LOGRÓ!!",  align="center", font=("Arial", 40, "bold")) 

    update()
    ontimer(draw, 100)



shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

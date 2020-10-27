import turtle
import math

def mandelbrot(z , c , n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1)
    else:
        return z ** 2 + c

# mida de la pantalla
screenx, screeny = 800, 600

# limits del pla complexe
complexPlaneX, complexPlaneY = (-2.0, 2.0), (-1.0, 2.0)

# precisio del dibuix
step = 2

# turtle config
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)
turtle.bgcolor("white")
screen = turtle.Screen()
screen.title("Mandelbrot Fractal (discretization step = %d)" % (int(step)))
mTurtle = turtle.Turtle()
mTurtle.penup()

# px * pixelToX = x en coordenades del pla complexe
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# plot
for px in range(-screenx//2, screenx//2, int(step)):
    for py in range(-screeny//2, screeny//2, int(step)):
        x, y = px * pixelToX, py * pixelToY
        m =  mandelbrot(0, x + 1j * y)
        if not math.isnan(m.real):
            color = [abs(math.sin(m.imag)) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(px, py)
    turtle.update()

turtle.mainloop()

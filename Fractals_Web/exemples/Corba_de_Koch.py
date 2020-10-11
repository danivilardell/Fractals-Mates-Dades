"""
        *****        FRACTALS AMB PYTHON        *****

L'objectiu d'aquest document es mostrar com es poden generar fractals utilitzant Python 3 i una petita llibreria grafica anomenada turtle.

EXEMPLE 1: LA CORBA DE KOCH

La corba de Koch es un dels primers fractal que es van descriure, i destaca per la seva simplicitat. Te aquesta forma (en funcio de n):

n=0

                    __________________

n=1
                            /\
                           /  \
                     _____/    \______

n=2
                          __/\__
                          \    /
                    __/\__/    \__/\__

n>2? Descobreix-ho executant el programa amb diferents n's.

CODI:
"""

# Importem la llibreria turtle
import turtle

"""
Definim la funcio recursiva Koch, la qual generara la corba de Koch
t: la "variable tortuga" amb la que volem fer el dibuix del fractal
n: el grau de complexitat del fractal
mida: nomes quan n=0, es la distancia de la linia que dibuixa la tortuga
"""
def Koch(t, n, mida):
    if rec > 0:
        Koch(t, n-1, mida/3)
        t.left(60)
        Koch(t, n-1, mida/3)
        t.right(120)
        Koch(t, n-1, mida/3)
        t.left(60)
        Koch(t, n-1, mida/3)
    else:
        t.forward(mida)

# I, finalment, escollim els paràmetres i cridem la funció
def main(n):
    # la variable t sera la nostra tortuga
    t = turtle.Turtle()
    # Movem la tortuga abans de començar per tenir el dibuix centrat
    t.left(180)
    t.up()
    t.forward(300)
    t.down()
    t.left(180)
    t.color("blue")

    Koch(t, n, 3*200) # Cridem la funció

    turtle.done() # Indiquem que el dibuix està acabat

    del t

main(4)

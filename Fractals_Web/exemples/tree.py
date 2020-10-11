import turtle

def tree(branch, t):
    if branch > 0:
        t.color((0.1, 1-0.15*branch, 0.1))
        t.pensize(2*branch-1)

        t.forward(branch*15)
        t.right(30)
        tree(branch-1,t)
        t.left(60)
        tree(branch-1,t)
        t.right(30)
        t.up()
        t.backward(branch*15)
        t.down()

def main():
    t = turtle.Turtle()
    numBranches = 6 # Podeu canviar el número de branques
    t.left(90)
    t.up()
    t.backward(180)
    t.down()

    t.begin_fill()
    tree(numBranches, t)
    t.end_fill()

    cv = turtle.getcanvas()
    cv.postscript(file="file_name.ps", colormode='color')

    turtle.done()

main()

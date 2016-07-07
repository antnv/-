from drawman import *
from time import sleep


def f(x):
    return x*x


drawman_scale(50)
xf= -5.0
xl= 5.0
pen_up()
for y in range(-5,6,1):
    to_point(-8, y)
    pen_down()
    to_point(8, y)
    pen_up()
for x in range(-6,7,1):
    to_point(x, -8)
    pen_down()
    to_point(x, 8)
    pen_up()
change_color('red')
x = xf
to_point(x, f(x))
pen_down()
while x <= xl:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(10)
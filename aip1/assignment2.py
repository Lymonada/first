import turtle

xs = input('Enter the list of coefficients: ')
xs = [float(x) for x in xs[1:-1].split(",")]
q = float(input('Enter the quantization amount: '))
s = float(input('Enter the scaling factor: '))
xi = float(input('Enter the starting point: '))
xf = float(input('Enter the ending point: '))


def polynomial_points(xs,q,xi,xf):
    """Contructs a list
    'xs' is a list of coefficients, 'q' is the quantization amount,
    'xi' is the starting x, 'xf' is the ending x
    Returns a list of tuples representing the points on the given polynomial
    E.g., if the polynomial is x^2 + 10x − 2 and quantization is 5 and the
    starting x and ending x values are −10 and 10, the function returns
    the list [(−10, −2),(−5, 27),(0, −2),(5, 73),(10, 198)]"""
    equation = 0
    list_1= []
    while xi <= xf :
        for i in range(len(xs)):
            equation += (xs[i])*(xi**i)
        list_1.append((xi,equation))
        xi += q
        equation = 0 
    return list_1

def scale(list_2, s):
    """Scales a list of (x, y) coordinates 
    'list_2' is the list of points in the xy-plane,
    's' is the scaling factor
    Return a list of (x,y) coordinates by a particular scaling factor
    E.g., if the 'list_2' is [(1,1),(2,4),(3,0)] and the scaling 
    factor is 2, the function must return [(2,2),(4,8),(6,0)]"""
    for i in range(len(list_2)):
        list_2[i] = (list_2[i][0]*s, list_2[i][1]*s)
    return list_2

value = polynomial_points(xs,q,xi,xf)

final_value = scale(value, s)

print(final_value)

turtle.penup()
turtle.home()

for i in final_value:
    turtle.goto(i)
    turtle.pendown()

def draw_bar(width):
    """Draw a graph
    'width' is the width of the bar graph
    Draw a bar graph from the points in the final value
    E.g., if the width value is 20, it will draw the right half 10 pixels
    of the bar and draw the long body according to the y value in the 
    final value and draw the left half 10 pixels and fill the bar at the end"""
    for point in final_value:
        x, y = point
        turtle.penup()
        turtle.goto(x, 0)
        turtle.pendown()
        turtle.fillcolor('blue')
        turtle.begin_fill()
        turtle.forward(width/2)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
        turtle.end_fill()       

def getWidth(q, s):
    """Calculate the width
    'q' is the quantization amount, 's' is the scaling factor
    Calculate the width value according to the quantization amount
    E.g., if the quantization amount was 1 and quantization amount
    was 30, the width of the bar will be 20"""
    return 20 * q * s/30

draw_bar(getWidth(q,s))

turtle.exitonclick()
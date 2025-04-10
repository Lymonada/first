shape = input("Enter the shape: ")

if shape == 's':
    side=float(input("Enter the length of the side: "))
    area=(side)*(side)
elif shape == 'r':
    length=float(input("Enter the length of the rectangle: "))
    width=float(input("Enter the width of the rectangle: "))
    area=(length)*(width)
elif shape == 'c':



    
    radius=float(input("Enter the radius of the circle: "))
    area=3.14159265359*(radius)**2

print(f'The area is {area:.4f}')

import math

area = int(input('Enter the area: '))

print(f"Shapes with area {area}")
print("Shape        Dimensions    Perimeter")
print("---------    -----------   ---------")


for length in range(1, area):
    if area % length == 0:
        width = area // length
        if length <= width:
            real_w = str(width)
            real_l = str(length)
            rec = f'{real_l.rjust(5)}x{real_w.rjust(5)}'
            real_rec = rec.rjust(14)
            perimeter = 2*(length + width)
            real_p = f'{perimeter:.2f}'
            print(f'Rectangle {real_rec} {real_p.rjust(11)}')
            
for base in range(1, area):
    if (2*area) % base == 0:
        height = (2*area) // base
        if base <= height:
            real_h = str(height)
            real_b = str(base)
            tri = f'{real_b.rjust(5)}x{real_h.rjust(5)}'
            real_tri = tri.rjust(15)
            diag = (base**2 + height**2)**(1/2)
            perimeter = base + height + diag
            deci_p = perimeter - int(perimeter)
            x = f'{deci_p:.2f}'
            x = x[2:]
            result = f'{int(perimeter)}.{x}'
            r = result.rjust(11)
            print(f'Triangle {real_tri} {r}')


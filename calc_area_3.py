###### area of square calc ######
def calc_area_square(side_length):
    return  side_length ** 2

input_number = 2
output_number = calc_area_square(input_number)
print(f'calc_area_square({input_number}) = {output_number}')

###### area of circle calculation ######
def calc_area_circle(radius):
    if not isinstance(radius, (float, int)): # checking input type
        raise TypeError(f'radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'radius is {radius} but must be positive')
    return math.pi * radius ** 2


print('')

#Square—The area is the length of a side squared.
print('To calculate the area of a Square and Volume of a Cube')
s_length=float(input('Please enter the length of one of the sides of the Square: '))

def square_area(l):
    area=pow(l,2)
    return area
print('The area of the square is: ',square_area(s_length))

print('')
def cube_volume(l):
    volume=pow(l,3)
    return volume
print('The volume of the cube is: ',cube_volume(s_length))
print('')

#Rectangle—The area is the length multiplied by the width.
print('To calculate the area of a Rectangle')
r_length=float(input('Please enter the length of one of the sides of the Rectangle: '))
r_width=float(input('Please enter the width of one of the sides of the Rectangle: '))

rectangle_area=r_length*r_width
print('The are of the rectangle is: ',rectangle_area)
print('')

#Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
print('To calculate the Area of a Circle and Volume of a Sphere')
def circle_area(r):
    import math
    area=math.pi*pow(r,2)
    return area

def sphere_volume(r):
    import math
    volume=(4/3)* math.pi*pow(r,3)
    return volume

radius=float(input('Please enter the radius of the Circle and Sphere: '))

print('The area of the circle is: ',circle_area(radius))
print('The volume of the sphere is: ',sphere_volume(radius))
print('')

print ('Please enter a value to Calculate the Area of a Square and Circle,'); ('and to find the volume of a Cube and a Sphere')
value=float(input('Please enter the Value:'))
print('Square Area: ',square_area(value),'Cube Volume: ',cube_volume(value),'Circle Area: ',circle_area(value),'Sphere Volume: ',sphere_volume(value))
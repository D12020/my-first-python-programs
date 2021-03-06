# This program contains functions that evaluate formulas used in geometry.
#
# Saleem Alnawasreh
# August 31, 2017

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallegogram_area(b,h):
    a = b * h
    return a

def trapezoid_area(a,b,h):
    a = ((a + b) / 2)
    return a

def rectangular_prism_area(w,h,l):
    v = w * h * l
    return v

def cone_volume(r,h):
    v = math.pi * r**2 * h / 3
    return v

def sphere_volume(r):
    v = (4 / 3) * math.pi * r**3
    return v
def rectangular_prism_surface_area(w,h,l):
    sa = 2((w * l) + (h * l) + (h * w))
    return sa

def sphere_surface_area(r):
    sa = 4 * math.pi * r**2
    return sa

def hypotenuse(a,b):
    c = ((a**2) + (b**2))**(1/2)
    return c

    



# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))


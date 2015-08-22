# function for calculating area of a polygon
# formula (1 / 4) * n * (s ** 2) / tan(Ï€/n)
# where n = number of sides and s = length of each side

# We have to use pi here so importing math library
import math 

def area_polygon(sides, length):
    area_calc = ((1.0/4) * sides * (length ** 2)) / math.tan(math.pi / length)
    return area_calc

print "Area of polygon with sides = 7 and length= 3 inches is", area_polygon(7, 3), "square inches"

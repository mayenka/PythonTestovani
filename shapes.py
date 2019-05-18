from math import pi


# def ellipse_area(a, b):
#     """Given the lengths of the semi-major and semi-minor axes, returns the
#     area of the ellipse."""
#     return pi * a * b       #návratová hodnota


#jak napíše funkci začátečník
def ellipse_area():
    a = float(input('Zadej mi první poloosu'))
    b = float(input('Zadej mi druhou poloosu'))
    print('Obsah elipsy je', a * b * pi)

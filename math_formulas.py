import math


def discriminant(a, b, c):
    '''(real number, real number, real number) -> real number

    Given the real numeric values a, b, and c from a quadratic equation,
    return the discriminant calculated via the discriminant formula.

    >>> discriminant(2, 4, 6)
    -32
    >>> discriminant(1, 2, 1)
    0
    >>> discriminant(1, 0, -16)
    64
    '''
    # Calculate the discriminant.
    dct = b**2 - (4 * a * c)
    # Return the discriminant.
    return dct


def get_roots_quadratic(a, b, c):
    '''(real number, real number, real number) -> list

    Suppose that the quadratic equation follows this format:
    ax^2 + bx + c = 0, where a, b, c, and x are real numbers.
    Return the roots calculated via the quadratic formula.

    >>> get_roots_quadratic(1, 0, -9)
    [-3.0, 3.0]
    >>> get_roots_quadratic(2, 3, 1)
    [-1.0, -0.5]
    >>> get_roots_quadratic(1, 2, 1)
    [-1.0]
    >>> get_roots_quadratic(3, 3, 2)
    'No real roots.'
    '''
    # Calculate the discriminant.
    dct = discriminant(a, b, c)
    # If the discriminant is a positive integer,
    # calculate the denominator and root.
    if dct >= 0:
        denominator = 2 * a
        x1 = ((-b) - math.sqrt(dct)) / denominator
        roots = [x1]
        # If the discriminant is above zero,
        # calculate the second root.
        if dct > 0:
            x2 = ((-b) + math.sqrt(dct)) / denominator
            roots += [x2]
    #If the discriminant is negative, return no real roots.
    else:
        roots = 'No real roots.'
    # Return the roots.
    return roots


def get_circle_area(radius):
    '''(real number) -> real number

    Return the area of a circle, given its radius.

    REQ: radius >= 0

    >>> get_circle_area(0)
    0.0
    >>> round(get_circle_area(2), 2)
    12.57
    >>> round(get_circle_area(10), 2)
    314.16
    >>> round(get_circle_area(5.7), 2)
    102.07
    '''
    # Calculate the area of the circle.
    area = math.pi * (radius**2)
    # Return the area of the circle.
    return area


def get_cylinder_volume(radius, height):
    '''(real number, real number) -> real number

    Return the volume of a cylinder, given its base radius and height.

    REQ: radius, height >= 0
    '''
    # Calculate the base area.
    base_area = get_circle_area(area)
    # Calculate the volume of the cylinder.
    volume = base_area * height
    # Return the volume of the cylinder.
    return volume


def get_cylinder_surface_area(radius, height):
    '''(real number, real number) -> real number

    Return the surface area of a cylinder, given its base radius and height.

    REQ: radius, height >= 0
    '''
    # Calculate the total base areas.
    total_base_area = 2 * get_circle_area(area)
    # Calculate the total height areas.
    height_area = height * (2 * radius * math.pi)
    # Calculate the total surface area.
    surface_area = total_base_area + height_area
    # Return the surface area of the cylinder.
    return surface_area


def calculate_function_of_x(function, x_value):
    '''(str, real number) -> real number
    >>> calculate_function_of_x('3x', 4)
    12
    >>> calculate_function_of_x('y=8x+3', 2)
    19
    '''
    y_value = 0

    return y_value


if __name__ == '__main__':
    import doctest

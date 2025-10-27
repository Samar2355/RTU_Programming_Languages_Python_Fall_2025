"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

# TODO: import math
import math as math
def circle_area(radius):
    """Return the area of a circle given its radius."""
    circle_area = (math.pi)*(radius**2)
    return circle_area
    # TODO: implement formula using math.pi
    pass

if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    # TODO: ask for user input, call circle_area(), and print formatted result
    print(circle_area(radius))
    pass

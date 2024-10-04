# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: float | int, b: float | int, c: float | int) -> float | int:
    """
    Function to sum 3 numbers.

    Args:
        a (float | int): first number
        b (float | int): second number
        c (float | int): third number

    Returns:
        out (float | int): sum of a, b, and c
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp: float | int, desired_temp: float | int) -> str:
    """
    Function to return the status of the thermostat.

    Args:
        temp (float | int): current temperature
        desired_temp (float | int): desired temperature

    Returns:
        status (str): status of the thermostat
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status

def have_digits(s: str) -> int:
    """
    Checks if a string has digits in it.

    Args:
        s (str): string to check

    Returns:
        out (int): 1 if the string has digits, 0 otherwise
    """
    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
def area_of_rectangle(width: float | int, height: float | int) -> float | int:
    """
    Calculates the area of a rectangle.

    Args:
        width (float | int): width of the rectangle
        height (float | int): height of the rectangle

    Returns:
        area (float | int): area of the rectangle
    """
    return width * height

def perimeter_of_rectangle(width: float | int, height: float | int) -> float | int:
    """
    Calculates the perimeter of a rectangle.

    Args:
        width (float | int): width of the rectangle
        height (float | int): height of the rectangle

    Returns:
        perimeter (float | int): perimeter of the rectangle
    """
    return 2 * (width + height)
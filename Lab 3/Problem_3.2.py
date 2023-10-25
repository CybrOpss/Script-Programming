# Problem 3.2: Closest to zero

def closest_to_zero(number1,number2):

    if abs(number1) < abs(number2):
        return number1
    else:
        return number2

closest_to_zero(5,9)
closest_to_zero(3,-2)
closest_to_zero(2,2)

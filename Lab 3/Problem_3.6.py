# Problem 3.6: Summarizing even integers

def sum_of_even_integers():

    integer1 = int(input("Enter first integer: "))
    integer2 = int(input("Enter second integer: "))

    sum = 0

    if integer1 < integer2:
        for an_integer in range(integer1,integer2+1):
            if an_integer % 2 == 0:
                sum += an_integer
    else:
        return "Integer1 is larger than the second, try again loser!"        
    return sum

print(sum_of_even_integers())


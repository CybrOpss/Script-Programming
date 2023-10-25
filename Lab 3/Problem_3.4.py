# Problem 3.4: Finding the highest value

def highest(list):

    highest = list[0]

    for number in list:
        if number > highest:
            highest = number

    print(highest)

highest([5, 3])
highest([2, 8, 4, 3])
highest([-2, -5])
highest([42])
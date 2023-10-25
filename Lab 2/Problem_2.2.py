# Problem 2.2: Computing averages

def average(numbers):

    sum = 0
    number_of_numbers = 0

    for number in numbers:

        sum += number
        number_of_numbers += 1

    return sum // number_of_numbers

print(average([1,4,4]))
print(average([4,4,4,4]))
print(average([-2,2]))
     





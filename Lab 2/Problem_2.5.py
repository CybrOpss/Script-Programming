def string_with_numbers(number):

    string = "1"

    for i in range(2,number+1): #2,3
        string += "_" + str(i)
    return string


print(string_with_numbers(9))

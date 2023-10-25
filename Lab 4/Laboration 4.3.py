# Problem 4.3: Computing sums

def sums(the_list):

    dict = {}
    odd_sum = 0
    even_sum = 0

    for numb in the_list:
        if numb % 2 == 1:
            odd_sum += numb
            dict["odd"] = odd_sum
        else:
            even_sum += numb
            dict["even"] = even_sum

    dict["even"] = even_sum
    dict["odd"] = odd_sum
    dict["all"] = even_sum + odd_sum

    return dict

print(sums([1, 2, 3, 4, 5]))
print(sums([2, 4, 6]))
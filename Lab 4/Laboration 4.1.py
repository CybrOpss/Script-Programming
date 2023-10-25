# Problem 4.1: Comparing two lists

def are_equal(first_list,second_list):

    index = 0

    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if first_list[i] == second_list[i]:
                index += 1
    
        if index == len(first_list):
            return True
            
    return False

print(are_equal([1, 2, 3], [1, 2, 3]))
print(are_equal([1, 2, 3], [1, 2, 2]))
print(are_equal([1, 2, 3], [1, 2]))
print(are_equal([1, 2], [1, 2, 3]))
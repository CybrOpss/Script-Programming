# Problem 4.2: Changing a list

def change_to_highest(the_list): 

    largest_numb = 0
    index = -1

    for lists in the_list: 

        index += 1 

        for numb in lists: 
            if numb > largest_numb:
                largest_numb = numb

        the_list[index] = largest_numb
        
    print(the_list)

change_to_highest([[1,2,3],[5,4,3],[2,7,6]])

# Problem 3.5: Counting occurrences

def count(list, string):

    times = 0

    for letter in list:
        if string == letter:
            times += 1
    return times
            
print(count(["a","b","c"], "b"))
print(count(["a","b","c"], "e"))
print(count(["a","a","a"], "a"))
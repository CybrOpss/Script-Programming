# Problem 2.3: Computing sums

def sum_of_ints(sequence1,sequence2):

    sum1 = 0
    sum2 = 0

    for i in sequence1:
        sum1 += i 
    for i in sequence2:
        sum2 += i

    return sum1 + sum2

print(sum_of_ints([1,4,2],[2,-1]))
print(sum_of_ints([4, 4, 4, 4], []))
print(sum_of_ints([4, 4], [4, 4]))
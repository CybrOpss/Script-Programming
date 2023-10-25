# Problem 3.3: Closest to zero (again)

from Problem_3.2 import closest_to_zero #Namn "Problem_3.2 funkar ej, ändrar till något enklare så funkar det"

def closest_to_zero_4(arg1,arg2,arg3,arg4):
    
    var1 = closest_to_zero(arg1, arg2)
    var2 = closest_to_zero(arg3,arg4)

    if abs(var1) < abs(var2):
        return var1
    else: 
        return var2

print(closest_to_zero_4(5, 9, 2, 11))
print(closest_to_zero_4(0, 3, -2, 4))
print(closest_to_zero_4(2, 2, -2, 1))

#Problem 1.5: Displaying a more complex multiplication table

print("This program displays a multiplication table.")

multiplication_number = int(input("Enter the number for which the multiplication table should be shown:" ))
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

for i in range(lower_bound, upper_bound+1):
    result = i*multiplication_number
    print(str(i)+" * "+str(multiplication_number)+" = " + str(result))


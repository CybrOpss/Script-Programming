#Problem 1.4: Displaying a multiplication table

print("This program displays a multiplication table.")

multiplication_number = int(input("Enter the number for which the multiplication table should be shown:" ))

for i in range(0,10):
    result = i*multiplication_number
    print(str(i)+" * "+str(multiplication_number)+" = " + str(result))



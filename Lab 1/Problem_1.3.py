#Problem 1.3: Computing the average of multiple numbers

amount_numbers = int(input("How many numbers do you want to enter: "))
sum = 0

for i in range(amount_numbers):
    sum += int(input("Enter your numbers: "))

average = sum / amount_numbers
print(average)



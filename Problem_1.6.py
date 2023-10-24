#Problem 1.6: Computing products

print("This program computes the product of the integers in a range")

lower_number = int(input("Enter the lower number of the range: ")) # 3
upper_number = int(input("Enter the upper number of the range: ")) # 5

product = 1

for i in range(lower_number,upper_number+1):
    product *= i
print(product)


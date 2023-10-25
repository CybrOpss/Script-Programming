# Problem 4.4: A less simple calculator

def calculator():
    
    memory = []
    memory.append(int(input("Enter initial memory: ")))
    operation = input("Enter operation (add/sub/mul/div/undo/quit): ")
    
    while operation != "quit":

        if operation == "add":
            operand = int(input("Enter operand: "))
            memory.append(memory[-1] + operand)
            print(str(memory[-1]) + " is stored in memory.")
        elif operation == "sub":
            operand = int(input("Enter operand: "))
            memory.append(memory[-1] - operand)
            print(str(memory[-1]) + " is stored in memory.")
        elif operation == "mul":
            operand = int(input("Enter operand: "))
            memory.append(memory[-1] * operand)
            print(str(memory[-1]) + " is stored in memory.")
        elif operation == "div":
            operand = int(input("Enter operand: "))
            if operand == 0:
                print("Can't divide by zero, try again")
            else: 
                memory.append(memory[-1] / operand)
                print(str(memory[-1]) + " is stored in memory.")
        elif operation == "undo":
            if len(memory) == 1:
                print("There is nothing to undo.")
            else:
                del memory[-1]
                print(str(memory[-1]) + " is stored in memory.")
            
        operation = input("Enter operation (add/sub/mul/div/undo/quit): ")

    print("The program finished with " + str(memory[0]) +" in memory")

calculator()
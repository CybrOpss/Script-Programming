def calculator():

    memory = int(input("Enter initial memory: "))
    operation = input("Enter operation (add/sub/mul/div/quit): ")
    
    while operation != "quit":

        operand = int(input("Enter operand: "))

        if operation == "add":
            memory = memory + operand
            print(str(memory) + " is stored in memory.")
        elif operation == "sub":
            memory = memory - operand
            print(str(memory) + " is stored in memory.")
        elif operation == "mul":
            memory = memory * operand
            print(str(memory) + " is stored in memory.")
        elif operation == "div":
            if operand == 0:
                print("Can't divide by zero, try again")
            else: 
                memory = memory / operand
                print(str(memory) + " is stored in memory.")
            
        operation = input("Enter operation (add/sub/mul/div/quit): ")

calculator()
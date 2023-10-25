class Calculator:

    def __init__(self, initial_memory_value):
        self.memory_value = []
        self.memory_value.append(initial_memory_value)

    def get_memory_value(self):
        return self.memory_value[-1]

    def add(self, operand):
        self.memory_value.append(self.memory_value[-1] + operand) 

    def subtract(self, operand):
        self.memory_value.append(self.memory_value[-1] - operand)

    def multiply(self, operand):
        self.memory_value.append(self.memory_value[-1] * operand)

    def divide(self, operand):
        self.memory_value.append(self.memory_value[-1] / operand)

    def undo(self):
        del self.memory_value[-1]

    def can_undo(self):
        if len(self.memory_value) <= 1:
            return False
        else: 
            return True

initial_memory_value = int(input("Enter initial memory value: "))
calculator = Calculator(initial_memory_value)

operation = ""

while operation != "quit":
	
	operation = input("Enter operation (add/sub/mul/div/undo/quit): ")
	
	if operation == "undo":
		if calculator.can_undo():
			calculator.undo()
			print(str(calculator.get_memory_value())+" is stored in memory.")
		else:
			print("There is nothing to undo.")
	elif operation != "quit":
		
		operand = int(input("Enter operand: "))
		
		if operation == "add":
			calculator.add(operand)
		elif operation == "sub":
			calculator.subtract(operand)
		elif operation == "mul":
			calculator.multiply(operand)
		elif operation == "div":
			calculator.divide(operand)
		
		print(str(calculator.get_memory_value())+" is stored in memory.")

print("The program finished with "+str(calculator.get_memory_value())+" in memory.")
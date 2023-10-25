# Problem 5.2: Improving the calculator

import xml.etree.ElementTree as ET

def calculator():
    
    memory = []
    memory.append(int(input("Enter initial memory: ")))
    operation = input("Enter operation (add/sub/mul/div/undo/store/quit): ")
    
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
        elif operation == "store":
            with open("memory.xml","w") as file:
                memory_list_element = ET.Element("MemoryList")
                for i in memory:
                    memory_element = ET.SubElement(memory_list_element, "Memory")
                    memory_element.text = str(i)
                xml_string = ET.tostring(memory_list_element, encoding="unicode")
                file.write(xml_string)
        elif operation == "load":
            memory = []
            with open("memory.xml", "r") as xml_file:
                xml_strings = xml_file.read()
                memory_list_elements = ET.fromstring(xml_strings)

            for i in memory_list_elements:
                memory.append(int(i.text))
            
        operation = input("Enter operation (add/sub/mul/div/undo/store/quit): ")

    print("The program finished with " + str(memory[-1]) +" in memory")

calculator()
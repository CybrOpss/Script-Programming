# Problem 2.4: Practising multiplication

from random import*

def practising_multiplication():

    multiplication_table = int(input("Enter a multiplication table: "))
    questions = int(input("Enter number of questions: "))
    
    for i in range(questions):
        random = randint(0,10)
        print("What is "+ str(multiplication_table)+" * "+ str(random))
        int(input("Enter answer: "))
        print("Correct answer: "+str(multiplication_table*random))
    
    return "\nThe exercise is now finished.\n"
    
print(practising_multiplication())



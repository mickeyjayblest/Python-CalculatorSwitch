class Calculator:
    def __init__(self, choice, num1, num2):
        self.choice = choice
        self.num1 = num1
        self.num2 = num2
        self.__total = None
    # this method controls the user decisions and inputs to calculate
    def switcher(self):
        choice_dict = {
            '1': 'add',
            '2': 'sub',
            '3': 'mult',
            '4': 'div',
            'a': 'add',
            's': 'sub',
            'm': 'mult',
            'd': 'div'
        }
        result_choice = choice_dict.get(self.choice, 'invalid choice input') # gets the choice for evaluation
        if result_choice == "add":
            self.__total = self.add(self.num1, self.num2)
        elif result_choice == "sub":
            self.__total = self.sub(self.num1, self.num2)
        elif result_choice == "mult":
            self.__total = self.mult(self.num1, self.num2)
        elif result_choice == "div":
            self.__total = self.div(self.num1, self.num2)
        else:
            self.__total = result_choice

    # the add  utility method
    def add(self, num1, num2):
        print("%s + %s: " % (num1, num2))
        return num1 + num2

    # the subtraction utility method
    def sub(self, num1, num2):
        print("%s - %s: " % (num1, num2))
        return num1 - num2

    # the multiplication utility method
    def mult(self, num1, num2):
        print("%s * %s: " % (num1, num2))
        return num1 * num2

    # the division utility method
    def div(self, num1, num2):
        if num2 == 0:
            return "can't divide by zero (0)"
        print("%s / %s: " % (num1, num2))
        return num1 / num2

    # utility for printing out the result
    def print_result(self):
        return self.__total


# runs on the main
if __name__ == "__main__":
    quitting = False
    while not quitting: # continues to loop until user quit
        print("Enter between 1-4 or a, s, m, d")
        print("1 or a to add\t2 or s to subtract\n3 or m to multiply\t4 or d to divide")
        print()
        try:
            userinput_choice = input("Enter what to calculate here: " )
            userinp1, userinp2 = input("Enter digits here i.e 5 15: ").split()
            userInput1 = float(userinp1)
            userInput2 = float(userinp2)
            """x, y, z = input("Enter your Input").split()
            userinput_choice = x
            userInput1 = float(y)
            userInput2 = float(z)"""
        except (ValueError, TypeError):
            print("Error in user Input")
        else:
            calc = Calculator(userinput_choice, userInput1, userInput2)
            calc.switcher()
            result = calc.print_result()
            print(f"{result} \n")

        print("Do you wish to make another calculation?")
        print("Y/y for yes N/n or quit to quit program")
        terminate = input("enter your decision here: ")
        if terminate.lower() in ['y', 'yes']:
            quitting = False
        elif terminate.lower() in ['n', 'no', 'quit']:
            print("Program terminated")
            quitting = True
        else:
            while True:  # this only run if the program doesnt understand the user choice to quit or continue
                #  it loops until the correct choice is entered
                print("\nY/y for yes N/n or quit to quit program")
                terminate = input("enter your decision here: ")
                if terminate.lower() in ['y', 'yes']:
                    quitting = False
                    break
                elif terminate.lower() in ['n', 'no', 'quit']:
                    print("\n\nProgram terminated")
                    quitting = True
                    break






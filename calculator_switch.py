class Calculator:
    def __init__(self, choice, num1, num2):
        self.choice = choice
        self.num1 = num1
        self.num2 = num2
        self.__total = None

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
        result_choice = choice_dict.get(self.choice, 'invalid choice input')
        if result_choice == "add":
            self.__total = self.add(self.num1, self.num2)
        elif result_choice == "sub":
            self.__total = self.sub(self.num1, self.num2)
        elif result_choice == "mult":
            self.__total = self.mult(self.num1, self.num2)
        elif result_choice == "div":
            self.__total = self.div(self.num1, self.num2)

    def add(self, num1, num2):
        print("%s + %s: " % (num1, num2))
        return num1 + num2

    def sub(self, num1, num2):
        print("%s - %s: " % (num1, num2))
        return num1 - num2

    def mult(self, num1, num2):
        print("%s * %s: " % (num1, num2))
        return num1 * num2

    def div(self, num1, num2):
        if num2 == 0:
            return "can't divide by zero (0)"
        print("%s / %s: " % (num1, num2))
        return num1 / num2

    def print_result(self):
        return self.__total


if __name__ == "__main__":
    print("Enter between 1-4 or a, s, m, d")
    print("1 or a to add\t2 or s to subtract\n3 or m to multiply\t4 or d to divide")
    print()

    try:
        x, y, z = input("Enter your Input").split()
        userinput_choice = x
        userInput1 = float(y)
        userInput2 = float(z)
    except (ValueError, TypeError):
        print("Error in user Input")
    else:
        calc = Calculator(userinput_choice, userInput1, userInput2)
        calc.switcher()
        result = calc.print_result()
        print(f"{result}")
    finally:
        print("\n\n\n\nCode by  Micheal codejavu")

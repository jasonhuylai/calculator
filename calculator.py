#Simple Calculator - OOP programming


#All math functions stored in this class
class Operator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)


#Program starts
def main():

    while True:

        # Numbers input
        num1 = float(input('Please enter the first number!'))
        num2 = float(input('Please enter the second number!'))

        # Create object for Operator() class
        operator = Operator(num1, num2)

        #Variable with an empty string
        math_option = ''

        while math_option not in ('+', '-', '*', '/'):

            #Calculates num1 and num2 based on the string value of math_option.
            #It will prompt user again if there is no +, -, *, or / input.
            math_option = input('What do you want to do with these two numbers? Please enter +, -, *, or /.')

            if math_option == '+':
                operator.add()
                break
            elif math_option == '-':
                operator.sub()
                break
            elif math_option == '*':
                operator.mul()
                break
            elif math_option == '/':
                operator.div()
                break


        #Use again or close calculator
        use_again = input('Do you want to try again?  Enter n to close the program.')

        if use_again == 'n':
            break




if __name__ == '__main__':
    main()
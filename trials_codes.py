class Calculations():
    def __init__(self):
        self.answer = 0
        self.calc_answer = 0
        self.sub_answer = 0

    def additions(self, num1, num2):
        self.answer = num1 + num2
        return self.answer

    def multiplications(self, calc1, calc2):
        self.calc1 = calc1
        self.calc2 = calc2
        calc_answer = calc1 * calc2
        return calc_answer

    def subtractions(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2
        sub_answer = sub1 - sub2
        return sub_answer


def main():
    test_calculations = Calculations()
    user_num1 = int(input("Enter first number: "))
    user_num2 = int(input("Enter second number: "))
    print(f"enter between 1. *  2. +  3. - ")
    user_select = input("Enter selection: ")
    if user_select == '*':
        final_answer = test_calculations.multiplications(user_num1, user_num2)
    elif user_select == "+":
        final_answer = test_calculations.additions(user_num1, user_num2)
    elif user_select == "-":
        final_answer = test_calculations.subtractions(user_num1, user_num2)
    else:
        print("Invalid operation in the simple calculator")
    print(f"Your final answer is: {final_answer}")



if __name__ == '__main__':
    main()

    



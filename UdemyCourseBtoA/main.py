

def calc_sum(num1, num2):
    return num1 + num2


def calc_sub(num1, num2):
    return num1 - num2


def calc_mul(num1, num2):
    return num1 * num2


def calc_div(num1, num2):
    return num1 / num2


def calc_pow(num1, num2):
    return num1 ** num2


cur_operator = ["+", "-", "/", "*", "^"]

eq = 0
input_Number_1 = int(input("Enter Number : "))
input_command = input("Enter (e : exit) -OR- (c : clear) -OR- (input operator) : ")

while input_command[0] != "e":
    if input_command[0] == "c":
        input_Number_1 = int(input("Enter Number : "))
        input_command = input("Enter (e : exit) -OR- (c : clear) -OR- (input operator) : ")
        continue
    elif input_command not in cur_operator:
        print("your Command is Wrong!!\nPlease Enter Correct Command")
        input_command = input("Enter (e : exit) -OR- (c : clear) -OR- (input operator) : ")
        continue
    else:
        pass

    input_Number_2 = int(input("Enter Number : "))

    if input_command == "+":
        eq = calc_sum(input_Number_1, input_Number_2)
    elif input_command == "-":
        eq = calc_sub(input_Number_1, input_Number_2)
    elif input_command == "*":
        eq = calc_mul(input_Number_1, input_Number_2)
    elif input_command == "/":
        eq = calc_div(input_Number_1, input_Number_2)
    elif input_command == "^":
        eq = calc_pow(input_Number_1, input_Number_2)
    elif input_command == "?":
        pass
    else:
        print("the operator is False!!")
        input_command = "error"

    print(f"The result is : {eq}")
    input_Number_1 = eq
    input_command = input("Enter (e : exit) -OR- (c : clear) -OR- (input operator) : ")

exit(0)

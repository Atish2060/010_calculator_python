def add(first, second):
    a = first
    b = second
    return a + b


def sub(first, second):
    a = first
    b = second
    return a - b


def mul(first, second):
    a = first
    b = second
    return a * b


def div(first, second):
    a = first
    b = second
    return a / b


def calc(first, second, opt):
    a = first
    b = second
    if opt == "+":
        return add(a, b)
    elif opt == "-":
        return sub(a, b)
    elif opt == "*":
        return mul(a, b)
    elif opt == "/":
        return div(a, b)


mop = "y"
while mop == "y":
    print("\n"*20)
    first_num = int(input(" Please enter the first number: "))
    eop = "y"
    while eop == "y":
        option = input("Please choose an operation you wanted to perform:\n+\n-\n*\n/\n")
        if option == "+" or option == "-" or option == "*" or option == "/":
            second_num = int(input("Please enter the second number: "))
            res = calc(first_num, second_num, option)
            print(f"{first_num} {option} {second_num} = {res}")
            first_num = res

        else:
            print("Invalid Operator. Please choose the valid one: \n")
        cont = input("Do you want to continue: y for yes and n for No: ").lower()
        eop = cont

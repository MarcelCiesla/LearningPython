# Defining Funtion
def add(arg1, arg2):
    total = arg1 + arg2
    return total


out = add(2, 3)
print(out)


def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)


adder(10, 50)
print(adder(10, 30))


def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x


out1 = summ([10, 20, 30])
print(out1)


# Default Argument
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function.")


greetings("Evening")

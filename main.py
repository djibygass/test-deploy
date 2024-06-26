from functions import add, sub, multiply, divide


def main():
    a = 2
    b = 3

    print(f"Addition of {a} and {b} is {add(a, b)}")
    print(f"Subtraction of {a} and {b} is {sub(a, b)}")
    print(f"Multiplication of {a} and {b} is {multiply(a, b)}")
    print(f"Division of {a} and {b} is {divide(a, b)}")


if __name__ == "__main__":
    main()

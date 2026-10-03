def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main():
    try:
        number = int(input("Enter a non-negative integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if number < 0:
        print("Factorial is not defined for negative integers.")
        return

    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
def factorial(number):
    factorial1 = 1
    for x in range(1, number + 1):
        factorial1 = factorial1 * x
    return factorial1


number = int(input("enter your number : "))
print(factorial(number))









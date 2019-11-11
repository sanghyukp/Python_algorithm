def fact(num):
    factorial = 1
    if num < 0 :
        print("must be positive")
    elif num == 0 :
        print("factorial = 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        print(num, factorial)

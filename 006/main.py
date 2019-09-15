def f(n):
    if (n == 0):
        return
    print(n % 10)
    f(n//10)
    


if __name__ == "__main__":
    f(12345)

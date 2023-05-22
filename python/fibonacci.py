count = int(input("How many fibonacci numbers would you like to generate? "))
i = 1
if count == 0:
    fib = []
    print(fib)
elif count == 1:
    fib = [1]
    print(fib)
elif count == 2:
    fib = [1,1]
    print(fib)
elif count > 2:
    fib = [1,1]
    while i < (count - 1):
        fib.append(fib[i] + fib[i-1])
        i += 1
print(fib)


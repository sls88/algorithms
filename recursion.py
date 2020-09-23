def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        return countdown(i-1)

countdown(5)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))

def sum2(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum2(arr[1:])

print(sum2([1, 2, 3, 4, 5]))

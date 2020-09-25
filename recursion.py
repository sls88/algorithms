def countdown(i):
    print(i, end=" ")
    if i <= 0:
        return
    else:
        return countdown(i-1)

countdown(5)
print()

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(12))

def sum2(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum2(arr[1:])

print(sum2([1, 2, 3, 4, 5]))

def max2(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] > max2(arr[1:]):
            return arr[0]
        else:
            return max2(arr[1:])

print(max2([1, 2, 7, 4, 5, 3, 12, 100]))

def counter(arr):
    if not arr:
        return 0
    else:
        return 1 + counter(arr[1:])

print(counter([1, 2, 7, 4, 5]))
print()
def bin_search(count, arr):
    x = int(len(arr)/2)
    a = arr[:x]
    b = arr[x+1:]
    if not arr:
        return None
    elif count == arr[x]:
        return x
    else:
        if arr[x] > count:
            return bin_search(count, a)
        else:
            if bin_search(count, b) is None:
                return None
            return bin_search(count, b) + len(a) + 1


s = [1, 2, 3, 6, 12]
print(bin_search(13, s))


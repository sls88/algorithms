import random

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.randint(0, len(arr)-1)
        l_pivot = []
        h_pivot = []
        for i in arr:
            if i <= arr[pivot]:
                l_pivot.append(i)
            else:
                h_pivot.append(i)

        return quick_sort(h_pivot) + quick_sort(l_pivot)


s = [1, 3, 6, 100 ,9 ,19, 55, 2, 16, 4, 0, -1, -219]
p = [2, 4, 1, 8]
print(quick_sort(s))
print(quick_sort(p))

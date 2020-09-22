def ind_smallest(arr):
    smallest = arr[0]   # для хранения наименьшего значения
    smallest_index = 0  # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr): # сортирует массив
    new_arr = []
    for i in range(len(arr)):
        smallest = ind_smallest(arr)    # находит наименьший элемент в масиве
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))
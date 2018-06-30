def push_front(arr, val):
    for item in range(len(arr), len(arr)-1):
        arr[item+1] = arr[item]
    arr[0] = val
    return arr

array = [1,2,3,4,5,6]
print(push_front(array, 0))
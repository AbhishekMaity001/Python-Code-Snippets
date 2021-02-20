
def swap(a, b, arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]

def Quick_Sort(arr, start, end) :
    if start < end:
        loc = partition(arr, start, end)
        Quick_Sort(arr, start, loc - 1)
        Quick_Sort(arr, loc + 1, end)

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end :
        while start < len(arr) and arr[start] <= pivot :
            start = start + 1

        while arr[end] > pivot:
            end = end - 1

        # swap when both start and end are not crossed!!
        if start < end:
            swap(start, end, arr)

    # swap when both are crossed!!
    swap(pivot_index, end, arr)

    return end


if __name__ == '__main__' :
    arr = [0,-1,-3,98] # [-5,55,24,6,9,88,2,6,0] # [11, 9, 29, 7, 2, 15, 28]
    Quick_Sort(arr, 0, len(arr)-1)
    print(arr)
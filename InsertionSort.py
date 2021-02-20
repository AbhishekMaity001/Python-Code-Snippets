import numpy as np
lst = [] # calculating the running median of the list
def Insertion_Sort(arr):
    for i in range(len(arr)):
        if i > 0:
            lst.append(np.median(arr[:i]))
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    lst.append(np.median(arr))

    print(lst)

            # print(arr[j])

# [11,91,29,7,2,15,28]
# 0, 1, 2, 3, 4, 5, 6
# i = 0
# i = 1, j = 0
# i = 2, j = 0,1
# i = 3, j = 0,1,2
# i = 4, j = 0,1,2,3
# i = 5, j = 0,1,2,3,4



if __name__ == '__main__':
    arr = [2,1,5,7,2,0,5] # [0,-9,-3,5,2,1,99,709] #[11,9,29,7,2,15,28]
    Insertion_Sort(arr)
    print(arr)
def linear_search(num_list, num_to_find) :
    for index, element in enumerate(num_list):
        if num_list[index] == num_to_find:
            return index

    return -1

def binary_search(num_list, num_to_find) :
    left = 0
    right = len(num_list)-1
    mid_index = 0

    while left <= right :
        mid_index = (left + right)//2
        mid_value = num_list[mid_index]

        if mid_value == num_to_find:
            return mid_index

        if mid_value < num_to_find :
            left = mid_index+1
        else :
            right = mid_index-1

    return "Not found!!"

def binary_recursion(num_list, num_to_find, left_index, right_index):

    if right_index < left_index :
        return -1
    mid_index = (right_index + left_index)//2
    if mid_index >= len(num_list) or mid_index < 0:
        return -1

    mid_number = num_list[mid_index]

    if mid_number == num_to_find:
        return mid_index
    if mid_number < num_to_find:
        left_index = mid_index +1
    else :
        right_index = mid_index - 1

    return binary_recursion(num_list, num_to_find, left_index, right_index)



if __name__ == '__main__' :
    numbers = [1,22,33,44,55,66,77,88,99]
    # print(binary_search(numbers, 22))
    index = binary_recursion(numbers, 100, 0, len(numbers))
    print(index)

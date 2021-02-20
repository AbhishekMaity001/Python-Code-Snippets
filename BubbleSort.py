def bubble_sort(elements):
    size = len(elements)

    for k in range(size-1):
        for i in range(size-1-k):
            if elements[i] > elements[i+1] :
                temp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = temp


if __name__ == '__main__' :
    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)
#24/6/18 - Samuel McHale - Resource containing sorting algorithms

def bubbleSort(items):
    complete = False
    while complete == False:
        swaps = 0
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                swaps += 1
                items[i], items[i+1] = items[i+1], items[i]
        if swaps == 0:
            complete = True
    return items

def quickSort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quickSort(x[:i])
        second_part = quickSort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

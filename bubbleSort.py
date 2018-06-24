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


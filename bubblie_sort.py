def bubblie_sort(num):
    n = len(num)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j+1] = num[j + 1], num[j]
                swap = True
        if not swap:
            break
    return num


listOfNumber = [90, 1, 55, 7, 18, 20, 32]
sortedList = bubblie_sort(listOfNumber)
print(sortedList)

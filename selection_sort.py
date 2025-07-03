def selection_sort(number):
    n = len(number)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if number[j] < number[min_index]:
                min_index = j
        number[i], number[min_index] = number[min_index], number[i]
    return number


listOfNumber = [29, 10, 14, 37, 13]
print('unsorted list is :', listOfNumber)
sorted_number = selection_sort(listOfNumber)
print('sorted list :', sorted_number)

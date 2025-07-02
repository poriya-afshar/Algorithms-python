def binary_serch(numebr, target):
    low = 0
    high = len(numebr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = numebr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

listOfNumber = [1, 3, 4, 5, 7, 11, 25, 36, 44]
target = 1
result = binary_serch(listOfNumber, target)
if result != -1:
    print(f'the number {target} was found at position {result} in the list')
else:
    print(f'the number {target} is not in the list.')

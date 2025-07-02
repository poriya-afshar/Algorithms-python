def merge_sort(listOfNumber):
    if len(listOfNumber) <= 1:
        return listOfNumber

    mid = len(listOfNumber) // 2
    left = merge_sort(listOfNumber[:mid])
    right = merge_sort(listOfNumber[mid:])
    return merge(left, right)


def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])

    return result


unsortedlist = [8, 5, 1, 6, 9, 12, 7, 13, 70, 65, 56, 45, 54, 33, 25]
sorted = merge_sort(unsortedlist)
print("sorted list :", sorted)


def linear_search(array,target):

    for index in range(len(array)):
        if array[index] == target:
            return index
        
    return 'not found'

listOfNumber = [4, 6, 7, 2, 9, 10, 23, 42]

result = linear_search(listOfNumber,1)
print(f'index : {result}')

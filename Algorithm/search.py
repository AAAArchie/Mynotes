def search(array,target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        if target < array[mid]:
            right = mid - 1
        if target > array[mid]:
            left = mid + 1
    return -1


print(search([1,2,3,4,5,6,7],4))


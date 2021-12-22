# sort list using mergesort
def mergesort(list):
    # allocate auxiliary array
    aux = [None] * len(list)

    # call recursive mergesort function
    mergesortr(list, 0, len(list) - 1, aux)

# perform mergesort using recursive algorithm
def mergesortr(list, low, high, aux):
    if low >= high:
        return
    mid = low + (high - low) // 2

    # left half
    mergesortr(list, low, mid, aux)

    # right half
    mergesortr(list, mid+1, high, aux)

    merge(list, low, mid, high, aux)

# merge list[low-mid] & list[mid+1-high] in sorted order 
def merge(list, low, mid, high, aux):
    # copy to auxiliary array
    for i in range(low, high + 1):
        aux[i] = list[i]
    
    left = low
    right = mid + 1
    index = low

    # loop through aux and put min(aux[left], aux[right]) back into list
    while index <= high:
        # if left pointer is past bounds, add aux[right] to list
        if left > mid:
            list[index] = aux[right]
            right += 1
        
        # if right pointer is past bounds, add aux[left] to list
        elif right > high:
            list[index] = aux[left]
            left += 1
        
        # put min(aux[left], aux[right]) back into list
        else:
            if aux[left] <= aux[right]:
                list[index] = aux[left]
                left += 1
            else:
                list[index] = aux[right]
                right += 1

        index += 1
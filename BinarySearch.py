def BinarySearch(num, val):
    first = 0
    last = len(num)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if num[mid] == val:
            index = mid
        else:
            if val<num[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
print(BinarySearch([10,20,30,40,50], 20))
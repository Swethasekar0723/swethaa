from heapq import heappop, heappush
def heap_sort(array):
    heap = []
    for element in array:
        heappush(heap, element)
        ordered = []
    while heap:
        ordered.append(heappop(heap))
    return ordered
array = [43, 56, 12, 6, 98, 23]
print(heap_sort(array))

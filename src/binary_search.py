def binSearch(xs: list[int], x: int):
    if not xs:
        return -1
        
    for i in range(1, len(xs)):
        if xs[i] < xs[i-1]:
            raise ValueError("Array must be sorted for binary search")
            
    left, right = 0, len(xs) - 1
    while left <= right:
        mid = (left + right) // 2
        if xs[mid] == x:
            return mid
        if xs[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binSearch(xs: list[int], x: int) -> int:
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

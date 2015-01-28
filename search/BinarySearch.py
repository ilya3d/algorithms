def binary_search( a, z ):
    lo = 0
    hi = n
    while lo < hi:
        mid = (hi + lo) // 2
        if z > a[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo
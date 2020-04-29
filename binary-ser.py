def BinarySea(x,nums):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high+low) // 2
        item = nums[mid]
        if item == x:
            CurrentTime = (datetime.now().time())
            return mid
        elif item > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

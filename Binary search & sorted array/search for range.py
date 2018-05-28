def searchForRange(vector:list, target:int) -> list:
    if vector.__len__() == 0:
        return [-1,-1]

    start = 0
    end = vector.__len__() - 1
    bound = [0,0]
    # search for left bound

    while start + 1 < end:
        mid = start + (end - start) // 2
        if vector[mid] == target:
            end = mid
        elif vector[mid] < target:
            start = mid
        elif vector[mid] > target:
            end = mid

    if vector[start] == target:
        bound[0] = start
    elif vector[end] == target:
        bound[0] = end
    else:
        bound[0] = bound[1] = -1
        return bound

    # Search for right bound
    start = 0
    end = vector.__len__() - 1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if vector[mid] == target:
            start = mid
        elif vector[mid] < target:
            start = mid
        elif vector[mid] > target:
            end = mid

    if vector[end] == target:
        bound[1] = end
    elif vector[start] == target:
        bound[1] = start
    else:
        bound[0], bound[1] = -1
        return bound

    return bound

if __name__ == '__main__':
    vector = [5,7,7,8,8,10]
    target = 8
    print(searchForRange(vector, target))
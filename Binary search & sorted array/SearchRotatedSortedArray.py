def SearchRotatedSortedArray(vector: list, target: int)->int:
    """
    画图！
    :param vector: 
    :param target:
    :return: 
    """
    start = 0
    end = vector.__len__() - 1

    while start + 1 < end:
        mid = start + (end - start) // 2

        if vector[start] < vector[mid]:
            if vector[start] <= target & target <= vector[mid]:
                end = mid
            else:
                start = mid

        else:
            if vector[mid] <= target & target <= vector[end]:
                start = mid
            else:
                end = mid

    if vector[start] == target:
        return start
    if vector[end] == target:
        return end

    return -1

if __name__ == '__main__':
    vector = [4,5,1,2,3]
    target = 2
    print(SearchRotatedSortedArray(vector, target))

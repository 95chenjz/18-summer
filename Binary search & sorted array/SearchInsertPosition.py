def SearchInsertPosition(vector:list, target:int) -> int:
    """
    第一个 >= target 的位置 / 最后一个 < target 的位置
    First postion of ...
    Last postion of ...
    :param vector: no duplicates
    :param target: inserted num
    :return: inserted position
    """
    if vector[0] >= target:
        return 0

    start = 0
    end = vector.__len__() - 1

    while start + 1 < end:
        mid = start + (end - start) // 2

        if vector[mid] == target:
            return mid

        elif vector[mid] < target:
            start = mid

        elif vector[mid] > target:
            end = mid

    if vector[end] == target:
        return end
    elif vector[end] < target:
        return  end + 1
    elif vector[start] == target:
        return start
    else:
        return  start +1

if __name__ == '__main__':
    vector = [1,3,5,6]
    target = 2
    print(SearchInsertPosition(vector, target))
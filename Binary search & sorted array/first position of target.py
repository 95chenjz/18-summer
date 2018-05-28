# Target: return the first position of target
# keys: 1. start + 1 < end
#       2. start + (end - start) / 2
#       3. A[mid] ==, <, >
#       4. A[start] A[end] ? target

def BinarySearch(vector: list, target: int) -> int:
    if vector.__len__() == 0:
        return -1

    start = 0
    end = vector.__len__()-1


    while(start + 1 < end):
        mid = start + (end - start) // 2
        if vector[mid] == target:
            end = mid
        elif vector[mid] < target:
            start = mid
        elif vector[mid] > target:
            end = mid

    if vector[start] == target:
        return start

    if vector[end] == target:
        return end

    return -1


if __name__ == '__main__':
    vector = [1,2,3,3,4,5,10]
    target = 3
    print(BinarySearch(vector, target))
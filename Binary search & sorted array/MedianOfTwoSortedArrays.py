import sys
def findmediansortedarrays(list1:list, list2:list):
    len = list1.__len__() + list2.__len__()
    if len % 2 == 0:
        return (findkth(list1, 0, list2, 0, len/2) + findkth(list1, 0, list2, 0, len/2+1)) / 2.0
    else:
        return findkth(list1, 0, list2, 0, len / 2 + 1)

def findkth(list1: list, start1, list2:list, start2, k):
    if start1 >= list1.__len__():
        return list2[start2 + k - 1]
    if start2 >= list2.__len__():
        return list1[start1 + k - 1]

    if k == 1:
        return min(start1, start2)

    key1 = list1[start1 + k // 2 - 1] if (start1 + k / 2 - 1) < list1.__len__() else sys.maxsize

    key2 = list2[start2 + k // 2 - 1] if (start2 + k / 2 - 1) < list2.__len__() else sys.maxsize


    if key1 < key2:
        return findkth(list1, start1 + k / 2, list2, start2, k - k / 2)
    else:
        return findkth(list1, start1, list2, start2 + k / 2, k - k / 2)

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    b = [2,3,4,5]
    print(findmediansortedarrays(a, b))

def missingNumber(arr):
    arr.sort()
    res = 1
    for num in arr:
        if num == res:
            res += 1
        elif num > res:
            break
    return res


if __name__ == "__main__":

    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))
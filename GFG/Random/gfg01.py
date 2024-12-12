from typing import List
class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        arrS=set(arr)
        if len(arr)==len(arrS):
            return [-1]
        arrS=list(arrS)
        for i in arrS:
            if i in arr:
                arr.remove(i)
        arr=list(set(arr))
        arr.sort()
        return arr

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr
    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    n = int(input())
    arr = IntArray().Input(n)
    obj = Solution()
    res = obj.duplicates(n, arr)
    IntArray().Print(res)
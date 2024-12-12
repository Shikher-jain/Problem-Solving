"""
        numBottles      numExchange         [~]               [ ]
             15             4           Fill bottle    Empty bottle
            [~][~][~]      [ ][ ][ ]         [~]          
            [~][~][~]      [ ][ ][ ]         [~]        [ ][ ]              
            [~][~][~]  ->  [ ][ ][ ]  ->     [~]   ->   [ ][ ]  ->  [~]  ->  [ ]  ->  O/P= len([~]) 
            [~][~][~]      [ ][ ][ ]        
            [~][~][~]      [ ][ ][ ]      [ ][ ][ ]     [ ][ ]     [ ][ ]   [ ][ ]

"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            print(numBottles,numExchange)
            ans += numBottles // numExchange
            print(ans)
            numBottles = numBottles // numExchange  + numBottles % numExchange
        # return ans

obj=Solution()
print(obj.numWaterBottles(15,4))
print(obj.numWaterBottles(9,3))
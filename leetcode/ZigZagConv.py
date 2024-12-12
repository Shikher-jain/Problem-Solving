class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        k = 0
        direction = (numRows == 1) - 1

        for c in s:
            rows[k] += c
            if k == 0 or k == numRows - 1:
                direction *= -1
            k += direction

        return ''.join(rows)

S0="PAYPALISHIRING"
S1="SHIKHER"
S2="SIHRHKE"
obj=Solution()
print(obj.convert(S0,int(input("Enter Rows no.: "))))
print(obj.convert(S1,int(input("Enter Rows no.: "))))
print(obj.convert(S2,int(input("Enter Rows no.: ")))) 
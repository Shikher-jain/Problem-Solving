class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below29 = ["",        "One",       "Two",      "Three",
                   "Four",    "Five",      "Six",      "Seven",
                   "Eight",   "Nine",      "Ten",      "Eleven",
                   "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["",      "Ten",   "Twenty",  "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def convert(num: int) -> str:
            if num < 20:
                s = below29[num]
            elif num < 100:
                s = tens[num // 10] + " " + below29[num % 10]
            elif num < 1000:
                s = convert(num // 100) + " Hundred " + convert(num % 100)
            elif num < 1000000:
                s = convert(num // 1000) + " Thousand " + convert(num % 1000)
            elif num < 1000000000:
                s = convert(num // 1000000) + " Million " + \
                convert(num % 1000000)
            else:
                s = convert(num // 1000000000) + " Billion " + \
                convert(num % 1000000000)
            return s.strip()
        return convert(num)
    
obj=Solution()
print(obj.numberToWords(1234))
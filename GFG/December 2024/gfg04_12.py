

class Solution:

    def areRotations(self,s1,s2):
        if len(s1) != len(s2):return False
        t = s1 + s1
        return s2 in t


        # s1 = abcd
        # t  = abcdabcd
        # s2 =    dabc
        # t  = abc dabc d
        
        # s1 = aab
        # t  = a aba ab
        # t  = aabaab
        # s2 =  aba
        
        # s1 = abcd
        # t  = abcdabcd
        # s2 = acbd
        


if __name__ == '__main__':


    s1 = str(input())
    s2 = str(input())
    if (Solution().areRotations(s1, s2)):
        print("true")
    else:
        print("false")


def twoSum(arr, target):
    seen = set()  
    for num in arr:
        complement = target - num  
        if complement in seen:
            return True            
        seen.add(num)
    return False  
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    x = int(input())
    arr = list(map(int, input().strip().split()))

    ans=twoSum(arr, x)
    if ans:
        print("true")
    else:
        print("false")
        #print("~")



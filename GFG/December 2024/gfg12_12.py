import bisect 

arr=[1,2,3,3,4,5,5,5,5,6]

tar=3
tar=5

l=bisect.bisect_left(arr,tar)
r=bisect.bisect_right(arr,tar)
print(f"Array: {arr} and Target: {tar}")
print(f"First Occurance at Index {l} and Last Occurance at Index {r}")
print(f"No. Of Occurance of {tar} is {r-l}")
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num  
        if complement in num_to_index:
            return [num_to_index[complement], i] 
        num_to_index[num] = i

    return []


ans=two_sum([1,2,3,4,5,6,7,8,9,10],45)
print(ans)
ans=two_sum([1,2,3,4,5,6,7,8,9,10],4)
print(ans)
ans=two_sum([1,2,3,4,5,6,7,8,9,10],30)
print(ans)
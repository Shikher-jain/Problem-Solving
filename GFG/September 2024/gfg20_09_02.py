def countBuildingsWithSunrise(a):
    ans = 1
    m = a[0]  
    for i in range(1, len(a)):
        if a[i] > m:
            ans += 1
            m = a[i] 
            
    return ans


heights = [7, 4, 8, 2, 9]
heights=[7, 7, 8, 3, 2, 8, 9, 7]
print(countBuildingsWithSunrise(heights))

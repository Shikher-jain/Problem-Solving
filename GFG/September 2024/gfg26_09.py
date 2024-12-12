heights = [1, 2, 3, 2, 5, 6, 7, 8, 5]
heights = [1, 2, 2, 3, 2]
heights = [1, 2, 3, 4]
heights = list()

if not heights:
    print(0)

    

Mstep = 0
Tstep = 0

for i in range(1, len(heights)):
    if heights[i] > heights[i - 1]:
        Tstep += 1
        Mstep = max(Mstep, Tstep)
    else:
        Tstep = 0
        
print(Mstep)
    

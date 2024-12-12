-1):
        # if mat[i][j]<
        if mat[i+1][j]<mat[i][j+1]:
            sum+=mat[i+1][j]
        print(mat[i][j] , end=" ")
    print()
print(sum)
# print(mat[0][0]+mat[r-1][c-1])
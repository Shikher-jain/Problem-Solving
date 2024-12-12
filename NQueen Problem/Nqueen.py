n=int(int(input("Enter no. of Queens : ")))

arr=[[0]*n]*n
def isSafe(arr,x,y,n):
    for row in range(x):
        if arr[row][y]==1:
            return False
    
    row=x;col=y
    while row>=0 and col>=0 :
        if arr[row][col]==1:
            return False
        row-=1;col-=1
        
    row=x;col=y
    while row>=0 and col<1 :
        if arr[row][col]==1:
            return False
        row-=1;col+=1

def nQueen(arr,x,n):
    if(x>=n):
        return True
    
    for col in range(n):
        if isSafe(arr,x,col,n):
            arr[x][col]=1

            if nQueen(arr,x+1,n):
                return True
            arr[x][col]=0 # BackTracking
    return False


if nQueen(arr,0,n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end="")
        print()

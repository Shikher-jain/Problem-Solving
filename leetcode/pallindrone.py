    # # # num=121
    # # # rev=0
    # # # temp=num
    # # # a=num%10;
    # # # rev=rev*10+a;
    # # # num=num/10;
    # # # print(rev)

    # # x=-121
    # # rev = x
    # # rev = str(rev)
    # # num = rev[::-1]
    # # if num == rev:
    # #     print("true")
    # #     # return "true"
    # # else:
    # #     print("false")
    # #     # return "false"

    # # x=121
    # # rev=0
    # # while x!=0:

    # num=--121
    # rev=0
    # temp=num
    # while num!=0:
    #     a=num%10;
    #     rev=rev*10+a;
    #     num=num//10;
    # print(rev)
    # print(temp)


    # x=-121
    # rev=0
    # temp=x
    # while x!=0:
    #     a=x%10
    #     rev=rev*10+a
    #     x=x//10
    # if temp == rev:
    #     return "true"
    # else:
    #     return "false"

    # x=-121
def pallindrone(x):
    if x < 0:
        return False
    rev = 0
    temp = x
    while x != 0:
        a = x % 10
        rev = rev * 10 + a
        x = x // 10
    return temp == rev
w=pallindrone(-121)
print(w)  
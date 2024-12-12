from collections import Counter
s1=list()
s2=list()
def solve(s,p):
    
    for i in p:
        if i not in s:
            print(-1)
            break
        tarP = Counter(p)
        print(tarP)
        tarS = Counter(s)
        print(tarS)
        print(s.index(i))
        s1.insert(s.index(i),i)
        s2.append(s.index(i))
    print(s1)
    print(s2)
    print(s[min(s2):max(s2)+1])
    # solve(s[min(s2)+1:max(s2)+1],p)

s = "timetopractice"
p = "toc"
solve(s,p)
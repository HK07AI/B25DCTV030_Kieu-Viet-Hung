day=list(map(int,input().split()))
n=int(input()  )
while n!=len(day):
    day=list(map(int,input().split()))
m=int(input())
g=[]
a=0
while m<=len(day):
    h=0
    for i in range(a,m):
        h+=day[i]
    g.append(h)
    a+=1
    m+=1
print(max(g)-min(g))

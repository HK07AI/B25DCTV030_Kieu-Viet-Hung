day=list(map(int,input().split()))
n=int(input()  )
while n!=len(day):
    day=list(map(int,input().split()))
j=int(input())
while j>0:
    i=0
    while i!=len(day) and j>0:
        j=j-day[i]
        i+=1
print(i)
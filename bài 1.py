day=list(map(int,input().split()))
day_sap_xep=sorted(day)
m=int(input()  )
a=2
l=0
while m <len(day_sap_xep):
    l+=day_sap_xep[m]
    m*=a
    a+=1
print(l)
        


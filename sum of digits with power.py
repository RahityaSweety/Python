n=153
nod=0
s=0
n1=n
org=n
while n>0:
    n=n//10
    nod=nod+1
sum1=0
while n1>0:
    digit=n1%10
    sum1=sum1+digit**nod
    n1=n1//10
if sum1==org:
    print("yes")
else:
    print("no")
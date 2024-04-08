m=int(input())
c=int(input())
p=int(input())
if m>80 and c>80 and p>80:
    print("A+")
elif m>60 and m<80 and c>60 and c>80 and p>60 and p<60:
    print("B+")
else:
    print("pass")
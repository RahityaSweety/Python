price=int(input("enter price"))
if price>=250 and price<300:
    print("recliners")
elif price>=150 and price<200:
    print("gold")
elif price>=100 and price<150:
    print("silver")
elif price>=200 and price<250:
    print("platinum")
else:
    print("balcony")
x=eval(input())
l=["t","r","u","e"]
l1=["l","o","v","e"]
count=0
count1=0
for j in x:
    for i in j:
        if i in l:
            count+=1

    for i in j:
        if i in l1:
            count1+=1
        
z=str(count)+str(count1)
print(z)
if int(z)>=90:
    print("Great Bonding!")
elif 70<=int(z)<90: 
    print("Need to make strong bond!")
elif 50<=int(z)<70:
    print("Will break in sometime!")
elif 30<=int(z)<50:
    print("Greater chance of breakup!")
else:
    print("Definitely Breakup!")
    

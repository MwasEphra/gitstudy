for num in range(1,11):
    if num%2==0:
        continue
    print(num)

x=0
while x<10:
    x+=1
    if x==5:
        continue
    print(x)

for y in range(1,11):
    if y==6:
        break
    print(y)

count=1
while True:
    print("Count:", count)
    if count==5:
        print("Condition met! Exiting loop")
        break
    count+=1

for i in range(0,10):
    if i==4:
        continue
    print(i)
    if i==9:
        break
print("loop interrupted")

a=0
while a<15:
    a+=1
    if a==7:
        continue
    print(a)
    if a==13:
        break
print("End of loop Execution")
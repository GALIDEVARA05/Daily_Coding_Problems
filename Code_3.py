#Prime Number
UI=int(input())
for i in range(2,UI):
    if UI%i==0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")
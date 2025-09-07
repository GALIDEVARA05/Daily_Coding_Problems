#Armstrong
UI=int(input("Enter any Number:"))
temp=UI
c=0
while temp!=0:
    c+=1
    temp//=10
s=0
temp=UI
while temp!=0:
    s+=((temp%10)**c)
    temp//=10
print("It Is Palindrome" if s==UI else "It Is Not a Palindrome")

#ArmStrong only for Positive Numbers
# import math
# UI=int(input("Enter any Number:"))
# Power=math.floor(math.log10(UI))+1
# temp=UI
# S=0
# while temp!=0:
#     S+=((temp%10)**Power)
#     temp//=10
# print("It Is Palindrome" if S==UI else "It Is Not a Palindrome")

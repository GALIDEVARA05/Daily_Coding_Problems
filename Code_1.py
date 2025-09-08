#palindrome
# palindrome is a word that reads from front and back the same
User_Input=input("Enter a Word:").lower()
l=0
r=len(User_Input)-1
for j in range(len(User_Input)//2): 
    if l<r and l!=r:
        if User_Input[j] == User_Input[r]:
            l+=1
            r-=1
        else:
            print("Not a Palindrome")
            break
else:
    print("The Given Word Is a Palindrome")
     
#changed the simpler code version
# User_Input=input("Enter a Word:")
# l=0
# r=len(User_Input)-1
# for j in range((len(User_Input)//2)): 
#         if User_Input[j] != User_Input[r-j]:
#             print("Not a Palindrome")
#             break
# else:
#     print("The Given Word Is a Palindrome")
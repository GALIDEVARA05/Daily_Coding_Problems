#palindrome
# palindrome is a word that reads from front and back the same
User_Input=input("Enter a Word:").upper()
l=0
r=len(User_Input)-1
for j in range((len(User_Input)//2)+1): 
    if l<r and l!=r:
        if User_Input[j] == User_Input[r]:
            l+=1
            r-=1
        else:
            print("Not a Palindrome")
            break
    else:
        print("The Given Word Is a Palindrome")
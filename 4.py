n=int(input("enter a positive number:"))
palindrome=0
number=n
while(n>0):
    digit=n%10
    palindrome=palindrome*10+digit 
    n=n//10
print("palindrome no",palindrome)
if number==palindrome:
    print("it is a palindrome number")
else:
    print("it is not a palindrome number")
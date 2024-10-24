num = 12321
#for commandline input
#num = int(input("enter the number:"))
rev = 0
while num > 0:
    rem = num % 10
    rev = (rev*10)+rem
    num = num//10
print("the reversed number is:", rev)

###palindrome
num = 12321
temp = num
rev = 0

while num > 0:
    rem = temp%10
    rev = (rev*10)+temp
    temp = temp//10

if num == rev:
    print("palindrome")
else:
    print("not palindrome")
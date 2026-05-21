'''Write a program to check Palindrome Number

 For example Number 12321 is a Palindrome Number, because 12321 is equal to its reverse Number 12321.

Steps for checking Palindrome number


1. Find reverse of the given number.
2. Compare that number with the reverse number.
3. If number and its reverse is equal then it is a Palindrome Number otherwise not.'''

num = int(input("Enter a number: "))

original_num = num
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

if original_num == reverse_num:
    print(original_num, "  is a Palindrome Number")
else:
    print(original_num, " not a Palindrome Number")
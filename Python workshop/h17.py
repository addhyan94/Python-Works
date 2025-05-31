# Flow control ke liye ....
'''
    Write a python program to find sum of digits of given number.
'''
n=eval(input("Enter a number = "))
s=0
a=abs(n) # abs ka use aapan ( - ) bali value ko (+) karne ke liye kar rahe hai jisse aapni value (+) me he aaye .......
while a > 0:
    d= a % 10
    s=s+d
    a=a//10
print("The sum of digit",n,"is = ",s)
# Flow control ke liye ....
'''
     Write a python program to reverse the digits of given number.
'''
n=eval(input("Enter a number = "))
rn =0
a=abs(n) # abs ka use aapan ( - ) bali value ko (+) karne ke liye kar rahe hai jisse aapni value (+) me he aaye .......
while a > 0:
    d= a % 10
    rn=rn*10+d
    a=a//10
    if n<0:
     rn=-rn
print("The Revers number is =",rn)
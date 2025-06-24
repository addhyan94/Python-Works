# WAP to accept marks of 6 students and display them in a sorted marnner .

marks = []
f1 = int(input("Enter the marks : "))
marks.append(f1)
f2 = int(input("Enter the marks : "))
marks.append(f2)
f3 = int(input("Enter the marks : "))
marks.append(f3)
f4 = int(input("Enter the marks : "))
marks.append(f4)
f5 = int(input("Enter the marks : "))
marks.append(f5)
f6 = int(input("Enter the marks : "))
marks.append(f6)

marks.sort()

print(marks)
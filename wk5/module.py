

#question1
import math


room_counts = int(input('How many rooms does the floor have?'))
total=0
for i in range(room_counts):
    length=float(input('room #%s length?'%(i+1)))
    width=float(input('room #%s width?'%(i+1)))
    total +=length*width
print ('total is ',total)

#question2
radius = float(input("Enter the radius of the circle : "))

circumference = 2 * math.pi * radius

print("Circumference of the circle is : %.2f" % circumference)


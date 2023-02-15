# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour.

import time
hour = int(time.strftime('%H'))
current = (time.strftime('%H:%M:%S'))

if (hour > 4 and hour < 12):
    print("Good Morning Sir, the time is", current)
elif (hour >= 12 and hour < 16):
    print("Good Afternoon Sir, the time is", current)
elif (hour >= 16 and hour < 20):
    print("Good Evening Sir, the time is", current)
elif (hour >= 20 and hour <= 23):
    print("Good Night Sir, the time is", current)
elif (hour >= 0 and hour <= 4):
    print("Good Night Sir, the time is", current)

    print("The International Literacy Day is observed on\n", "A.Sep 8\nB.Nov 28\nC.May 2\nD.Sep 22"),
    print("The language of Lakshadweep. a Union Territory of India, is\n", "A.Tamil\nB.Hindi\nC.Malayalam\nD.Telugu"),
#Countdown timer python

import time

my_time=int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds=x%60 #we do not want seconds to go over 60 seconds
    minutes=int(x/60)%60 #we do not want minutes to go over 60 minutes
    hours=int(x/3600)%24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")
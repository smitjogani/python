# Python Program to Create a Countdown Timer

import time

def countDown(time_sec):

    while time_sec:
        mins , secs = divmod(time_sec, 60)
        timeformate = '{:02d}{:02d}'.format(mins,secs)
        print(timeformate, end = '\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")
    
stp_time = int(input("Enter the second :"))
countDown(stp_time)


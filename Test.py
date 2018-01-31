# !/usr/bin/env python
from Tkinter import *
import time

start = int()
def machine():
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        return(final-start)

        # Send time to database

    def main():
        top = Tk()

        Start = Button(top, text ="Start", command = start_time)
        Stop = Button(top, text ="Stop", command = stop_time)
        Start.pack()
        Stop.pack()
        top.mainloop()
    main()
machine()
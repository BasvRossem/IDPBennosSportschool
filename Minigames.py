# !/usr/bin/env python
import mysql.connector
from Tkinter import *
import tkMessageBox
import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector
import time
import datetime

#Variables
start = int()
# def buttonCounter():
#
#     GPIO.setmode(GPIO.BCM)
#     print(info)
#     GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     counter = 0
#     while True:
#         input_state = GPIO.input(19)
#         if input_state == False:
#             counter += 1
#             print(counter)
#             time.sleep(0.5)

# def measureTime():
#     initial = 0
#
#     top = Tkinter.Tk()
#
#     def start_time():
#         global initial
#         tkMessageBox.showinfo("Timer", "The timer will now begin")
#         initial = time.time()
#         return initial
#
#     def stop_time():
#         # you could check for initial == 0 and display an error
#         final = time.time()
#         tkMessageBox.showinfo("Timer", final - initial)
#         return(final-initial)
#
#     Start = Tkinter.Button(top, text ="Start", command = start_time)
#     Stop = Tkinter.Button(top, text ="Stop", command = stop_time)
#     Start.pack()
#     Stop.pack()
#     top.mainloop()

def machine1(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (1,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine1Scherm = Tk()

        Start = Button(machine1Scherm, text="Start", command=start_time)
        Stop = Button(machine1Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine1Scherm.mainloop()

    main()

def machine2(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (2,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine2Scherm = Tk()

        Start = Button(machine2Scherm, text="Start", command=start_time)
        Stop = Button(machine2Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine2Scherm.mainloop()

    main()

def machine3(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (3,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine3Scherm = Tk()

        Start = Button(machine3Scherm, text="Start", command=start_time)
        Stop = Button(machine3Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine3Scherm.mainloop()

    main()

def machine4(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (4,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine4Scherm = Tk()

        Start = Button(machine4Scherm, text="Start", command=start_time)
        Stop = Button(machine4Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine4Scherm.mainloop()

    main()

def machine5(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (5,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine5Scherm = Tk()

        Start = Button(machine5Scherm, text="Start", command=start_time)
        Stop = Button(machine5Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine5Scherm.mainloop()

    main()

def machine6(personInfo):
    def start_time():
        print("Timer", "The timer will now begin")
        initial = time.time()
        global start
        start = initial
        return (initial)

    def stop_time():
        # Variables
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # you could check for initial == 0 and display an error
        final = time.time()
        print("Timer", final - start)
        difference = final - start

        # Select correct session
        cursor = cnx.cursor(buffered=True)
        now = datetime.datetime.now()
        datum = now.strftime("%Y-%m-%d")
        print(personInfo[0])
        print(datum)
        query = ("SELECT session_id, User_user_id FROM session WHERE '{}' = User_user_id AND date = '{}'".format(personInfo[0], datum))
        cursor.execute(query)

        for (session_id, User_user_id) in cursor:
            sessionId = session_id
            print("Jup")
            print(sessionId)
            # Send time to database
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ("INSERT INTO exercise_session (Exercise_exercise_id, Session_session_id, sets, reps, note) VALUES (6,'{}', 1, {}, 'Lekker stukje start/stop drukken')".format(sessionId, difference))
            cursor.execute(query)
            cnx.commit()
            cursor.close()

    def main():
        machine6Scherm = Tk()

        Start = Button(machine6Scherm, text="Start", command=start_time)
        Stop = Button(machine6Scherm, text="Stop", command=stop_time)
        Start.pack()
        Stop.pack()
        machine6Scherm.mainloop()

    main()

def main():
    print("Scan je kaart om te beginnen")
    personInfo = wieIsHet()
    print("Oke, {} {}, kies een apparaat".format(personInfo[1], personInfo[2]))

    print("1. Fiets")
    print("2. Crosstrainer")
    print("3. Krachtstation")
    print("4. Roeiapparaat")
    print("5. Loopband")
    print("6. Mechanische trap")

    choice = raw_input("Kies een nummer van 1 tot 6")

    if choice == "1":
        machine1(personInfo)
    elif choice == "2":
        machine2(personInfo)
    elif choice == "3":
        machine3(personInfo)
    elif choice == "4":
        machine4(personInfo)
    elif choice == "5":
        machine5(personInfo)
    elif choice == "6":
        machine6(personInfo)
    else:
        print("Kies iets wat mogelijk is")
    # root = Tk()
    #
    # machinenr1 = Button(text="Crosstrainer", command= lambda: machine1(personInfo))
    # machinenr1.pack()
    #
    # machinenr2 = Button(text="Krachtstation", command= lambda: machine2(personInfo))
    # machinenr2.pack()
    #
    # machinenr3 = Button(text="Mechanische trap", command= lambda: machine3(personInfo))
    # machinenr3.pack()
    #
    # machinenr4 = Button(text="Roeiapparaat", command= lambda: machine4(personInfo))
    # machinenr4.pack()
    #
    # machinenr5 = Button(text="Loopband", command= lambda: machine5(personInfo))
    # machinenr5.pack()
    #
    # machinenr6 = Button(text="Fiets", command= lambda: machine6(personInfo))
    # machinenr6.pack()
    #
    # root.mainloop()

def read():  # leest de data van de kaart
    reader = SimpleMFRC522.SimpleMFRC522()
    print("Plase provide RFID card")
    id, text = reader.read()
    return (text)

def wieIsHet(): #Asks the database who wants to login
    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')
    cursor = cnx.cursor(buffered=True)
    code = read()
    print(code)
    query = ("SELECT user_id, firstname, lastname  FROM user WHERE user.code = '{}'".format(code))
    cursor.execute(query)
    print(query)
    for (user_id, firstname, lastname) in cursor:
        return(user_id, firstname, lastname)
    cursor.close()

# def login():
#     print("Scan je kaart om te beginnen")
#     personInfo = wieIsHet()
#     print(type(personInfo))
#     kiesMachine(personInfo)
#     print("Oke, {} {}, kies een apparaat".format(personInfo[1], personInfo[2]))


main()
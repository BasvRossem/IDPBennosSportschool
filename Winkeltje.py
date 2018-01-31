# !/usr/bin/env python
import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector
import time
import tkMessageBox
from Tkinter import *

# leest de data van de kaart
def read():
    reader = SimpleMFRC522.SimpleMFRC522()
    print("Plase provide RFID card")
    id, text = reader.read()
    return (text)

#Asks the database who wants to login
def wieIsHet():
    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')
    cursor = cnx.cursor(buffered=True)
    code = read()
    print(code)
    query = ("SELECT user_id, firstname, lastname, points  FROM user, membership_registration WHERE user.code = '{}' and user_id = membership_registration.user_user_id".format(code))
    cursor.execute(query)
    print(query)
    for (user_id, firstname, lastname, points) in cursor:
        return(user_id, firstname, lastname, points)
    cursor.close()

def reducePoints(userId, points, cost):
    userId = userId
    points = points
    cost = cost
    newPoints = int()

    if points < cost:
        tkMessageBox.showinfo("User has not enough points to buy this.")
    else:
        newPoints = points - cost

        #Update the points in the db
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        cursor = cnx.cursor(buffered=True)
        print(newPoints)
        query = ("UPDATE membership_registration SET points ={} WHERE {} = user_user_id".format(newPoints, userId))
        cursor.execute(query)
        cnx.commit()
        tkMessageBox.showinfo("Transaction complete. please close this window.")

def main():
    personInfo = wieIsHet()
    userId = personInfo[0]
    firstName = personInfo[1]
    lastName = personInfo[2]
    points = personInfo[3]

    root = Tk()
    root.geometry("300x100")

    #Make database connection
    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT product_name, cost  FROM winkeltje")
    cursor.execute(query)

    userInfoLabel = Label(text="{} {} heeft {} punten".format(firstName, lastName, points))
    userInfoLabel.pack()

    for (product_name, cost) in cursor:
        productButton = Button(text="{} {} punten".format(product_name, cost), command= lambda cost=cost: reducePoints(userId, points, cost))
        productButton.pack()

    root.mainloop()

main()
# !/usr/bin/env python
import RPi.GPIO as GPIO
import SimpleMFRC522
import mysql.connector
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, 0)
GPIO.setup(20, GPIO.IN)

p = GPIO.PWM(4,50)
p.start(7.5)

def distance():
    #TRIG = 26
    #ECHO = 20
    oldDistance = 100
    while True:
        if oldDistance >= 50:
            time.sleep(0.1)

            GPIO.output(26, 1)
            time.sleep(0.00001)
            GPIO.output(26, 0)

            while GPIO.input(20) == 0:
                pass
            start = time.time()

            while GPIO.input(20) == 1:
                pass
            stop = time.time()
            distanceCm = ((stop - start) * 170) * 100
            oldDistance = distanceCm
            continue
        else:
            time.sleep(2)

            GPIO.output(26, 1)
            time.sleep(0.00001)
            GPIO.output(26, 0)

            while GPIO.input(20) == 0:
                pass
            start = time.time()

            while GPIO.input(20) == 1:
                pass
            stop = time.time()
            distanceCm = ((stop - start) * 170) * 100
            if distanceCm >= 50:
                break

def goingIn(): #poortje gaat open voor mensen die buiten staan
    p.ChangeDutyCycle(2.5)

def goingOut(): #poortje gaat open voor mensen die binnen staan
    p.ChangeDutyCycle(12.5)

def neutral(): #poortje gaat naar de gesloten/neutrale positie
    p.ChangeDutyCycle(7.5)

def sqlVraag(): #vraagt aan de database voor de status en locatie van de klant met behulp van de code
    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')
    cursor = cnx.cursor(buffered=True)
    code = read()
    query = ("SELECT user_id, status, locatie  FROM user, membership_registration WHERE user.code = '{}' and user_id = membership_registration.user_user_id".format(code))
    cursor.execute(query)
    for (user_id, status, locatie) in cursor:
        id = user_id
        old_status = status
        old_locatie = locatie
        print("{}, {}".format(status, locatie))
        if locatie == 1:
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            # Sql code om die 1 naar een 0 om te zetten
            query = ("UPDATE membership_registration SET locatie = 0 WHERE {} = user_user_id".format(id))
            cursor.execute(query)
            cnx.commit()
        elif locatie == 0:
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            # sql code om die 0 naar een 1 om te zetten
            query = ("UPDATE membership_registration SET locatie = 1 WHERE {} = user_user_id".format(id))
            cursor.execute(query)
            cnx.commit()

            #Chek if there is a session
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            now = datetime.datetime.now()
            datum = now.strftime("%Y-%m-%d")
            query = ("SELECT COUNT(1) FROM session WHERE '{}' = date AND '{}' = User_user_id".format(datum, id))
            cursor.execute(query)
            print("session check")
            if cursor.fetchone()[0] == False:
                #start new session
                #Add date to session together with user id
                cursor.close()
                cursor = cnx.cursor(buffered=True)
                now = datetime.datetime.now()
                date = now.strftime("%Y-%m-%d")
                query = ("INSERT INTO session (date, User_user_id) VALUES ( '{}', '{}')".format(date, id))
                cursor.execute(query)
                cnx.commit()

            #Select who gets the points
            cursor.close()
            cursor = cnx.cursor(buffered=True)
            query = ( "SELECT user_id, points  FROM user, membership_registration WHERE user.code = '{}' and user_id = membership_registration.user_user_id".format(code))
            cursor.execute(query)

            # Add 5 points
            for (user_id, points) in cursor:
                cursor = cnx.cursor(buffered=True)
                query = ("UPDATE membership_registration SET points ={} WHERE {} = user_user_id".format((int(points) + 5), user_id))
                cursor.execute(query)
                cnx.commit()
                cursor.close()

        return("{}, {}".format(old_status, old_locatie))
    cursor.close()

def read(): #leest de data van de kaart
    reader = SimpleMFRC522.SimpleMFRC522()
    print("Plase provide RFID card")
    id, text = reader.read()
    return(text)

try:
    while True:
        readText = sqlVraag()
        if readText == "actief, 1":
            goingOut()
            time.sleep(1)
            distance()
            neutral()
            time.sleep(1)
        elif readText == "actief, 0":
            goingIn()
            time.sleep(1)
            distance()
            neutral()
            time.sleep(1)
        else:
            print("You are not going anywhere, please get a staff member to help.")
            break

finally:
    GPIO.cleanup()
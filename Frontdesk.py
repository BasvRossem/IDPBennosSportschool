#!/usr/bin/env python
import random
import mysql.connector
import time
import datetime
import SimpleMFRC522
from Tkinter import *
from threading import Timer

#Make a function run every few seconds DONE
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

#Show how many users are in at the moment DONE
def aantalPersonenScherm():
    # Closes the window correctly DONE
    def on_closing():
        rt.stop()
        aantalPersonenScherm.destroy()

    # Count how many users are in at the moment
    def aantalPersonen():
        # Making a connection with the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')

        # Getting data from database
        cursor = cnx.cursor(buffered=True)
        query = ("SELECT user_user_id  FROM membership_registration WHERE locatie = 1")
        cursor.execute(query)

        #Variables
        count = 0

        # Counting the amount of users inside
        for (user_user_id) in cursor:
            count += 1

        cursor.close()
        display.configure(text="{}".format(count))

    rt = RepeatedTimer(1, aantalPersonen)

    aantalPersonenScherm = Tk()
    aantalPersonenScherm.geometry("200x100")
    aantalPersonenScherm.protocol("WM_DELETE_WINDOW", on_closing)

    Label(aantalPersonenScherm, text="Aantal mensen in de sportschool").grid(row=1, column=1)
    display = Label(aantalPersonenScherm, text="")
    display.grid(row=2, column=1, sticky=W)

    aantalPersonenScherm.mainloop()
    rt.stop()

#Write RFID code to card DONE
def showDetails():
    reader = SimpleMFRC522.SimpleMFRC522()
    dataString = (voorletterEntry.get() + tussenvoegselEntry.get() + achternaamEntry.get() + geboortedatumEntry.get() + straatEntry.get() + huisnummerEntry.get() + toevoegingEntry.get() + postcodeEntry.get() + woonplaatsEntry.get())
    randomDataString = "".join(random.sample(dataString, 48))
    print("Now place your tag to write")
    reader.write(randomDataString)
    return(randomDataString)
    GPIO.cleanup()

#Add a new user
def newUser():
    # Adds a user to the database and creates a new RFID card
    def addDataToDatabaseAndMakeANewCard():
        # Variables
        userId = int()
        addressId = int()
        # Make a connectin to the database
        cnx = mysql.connector.connect(user='root',
                                      password='Benno',
                                      host='xxx.xxx.xxx.xxx',
                                      database='db3242919')
        # Sql query to add address data to database
        cursor = cnx.cursor(buffered=True)
        query = (
            "INSERT INTO address (street_address, zipcode, city) VALUES ('{}', '{}', '{}')".format(
                "{} {}".format(streetEntry.get(), numberEntry.get()), zipcodeEntry.get(), cityEntry.get()))
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()

        # Sql query to find out what address id the address got
        cursor = cnx.cursor(buffered=True)
        query = (
            "SELECT address_id, city  FROM address WHERE '{}' = street_address AND '{}' = zipcode AND '{}' =  city".format(
                "{} {}".format(streetEntry.get(), numberEntry.get()), zipcodeEntry.get(), cityEntry.get()))
        print(query)
        cursor.execute(query)
        for (address_id, city) in cursor:
            addressId = address_id
        cursor.close()

        # Sql query to add user data to database
        cursor = cnx.cursor(buffered=True)
        query = (
        "INSERT INTO user (firstname, lastname, email, username, password) VALUES ('{}','{}','{}','{}','{}')".format(
            firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()

        # Sql query to find out what user id the user got
        cursor = cnx.cursor(buffered=True)
        query = (
        "SELECT user_id, email  FROM user WHERE '{}' = firstname AND '{}' = lastname AND '{}' =  email AND '{}' =  username".format(
            firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), usernameEntry.get()))
        print(query)
        cursor.execute(query)
        for (user_id, email) in cursor:
            userId = user_id
        cursor.close()

        # Sql query to connect the user and the address
        cursor = cnx.cursor(buffered=True)
        query = ("UPDATE `user` SET `address_id` = {} WHERE `user`.`user_id` = {}".format(addressId, userId))
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()

        # Make a RFID card for the user
        reader = SimpleMFRC522.SimpleMFRC522()
        dataString = "{}{}{}{}".format(firstnameEntry.get(), lastnameEntry.get(), emailEntry.get(), usernameEntry.get(),
                                       streetEntry.get(), numberEntry.get(), zipcodeEntry.get(), cityEntry.get())
        randomDataString = ''.join([random.choice(dataString) for _ in range(48)])
        print("Now place your tag to write")
        reader.write(randomDataString)
        print("Written")

        # Sql to add the user code to the database
        cursor = cnx.cursor(buffered=True)
        query = ("UPDATE user SET code = '{}' WHERE user.user_id = {}".format(randomDataString, userId))
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()

        # SQL to add the membership data to database
        now = datetime.datetime.now()
        vandaagdedag = now.strftime("%Y-%m-%d")
        cursor = cnx.cursor(buffered=True)
        query = ("INSERT INTO `membership_registration` (date, `status`, `Membership_membership_id`, `User_user_id`, `locatie`, `points`, `iban`) VALUES ('{}', 'actief', {}, '{}', '0', '100', '{}')".format(vandaagdedag, int(membershiptypeEntry.get()),userId, ibanEntry.get()))
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()
    newUserScreen = Tk()

    #Personal data to add
    firstnameLabel = Label(newUserScreen, text="Voornaam")
    lastnameLabel = Label(newUserScreen, text="Achternaam")
    emailLabel = Label(newUserScreen, text="Email")
    usernameLabel = Label(newUserScreen, text="Gebruikersnaam")
    passwordLabel = Label(newUserScreen, text="wachtwoord")

    firstnameEntry = Entry(newUserScreen)
    lastnameEntry = Entry(newUserScreen)
    emailEntry = Entry(newUserScreen)
    usernameEntry = Entry(newUserScreen)
    passwordEntry = Entry(newUserScreen)

    firstnameLabel.grid(row=0, sticky=E)
    lastnameLabel.grid(row=1, sticky=E)
    emailLabel.grid(row=2, sticky=E)
    usernameLabel.grid(row=3, sticky=E)
    passwordLabel.grid(row=4, sticky=E)

    firstnameEntry.grid(row=0, column=1)
    lastnameEntry.grid(row=1, column=1)
    emailEntry.grid(row=2, column=1)
    usernameEntry.grid(row=3, column=1)
    passwordEntry.grid(row=4, column=1)

    #Empty line so it looks better
    empty = Label(newUserScreen)
    empty.grid(row=5)

    #Address data to add
    streetLabel = Label(newUserScreen, text="Straat")
    numberLabel = Label(newUserScreen, text="Huisnummer")
    zipcodeLabel = Label(newUserScreen, text="Postcode")
    cityLabel = Label(newUserScreen, text="Woonplaats")

    streetEntry = Entry(newUserScreen)
    numberEntry = Entry(newUserScreen)
    zipcodeEntry = Entry(newUserScreen)
    cityEntry = Entry(newUserScreen)

    streetLabel.grid(row=6, sticky=E)
    numberLabel.grid(row=7, sticky=E)
    zipcodeLabel.grid(row=8, sticky=E)
    cityLabel.grid(row=9, sticky=E)

    streetEntry.grid(row=6, column= 1)
    numberEntry.grid(row=7, column= 1)
    zipcodeEntry.grid(row=8, column= 1)
    cityEntry.grid(row=9, column= 1)

    #Extra Shid i still had to add
    ibanLabel = Label(newUserScreen, text="IBAN")
    membershiptypeLabel = Label(newUserScreen, text="Soort membership")

    ibanEntry = Entry(newUserScreen)
    membershiptypeEntry = Entry(newUserScreen)

    ibanLabel.grid(row=10, sticky=E)
    membershiptypeLabel.grid(row=11, sticky=E)

    ibanEntry.grid(row=10, column= 1)
    membershiptypeEntry.grid(row=11, column= 1)

    #Button to make everything else happen
    sqlCodeButton = Button(newUserScreen, text="Gegereer nieuwe code", command=lambda: addDataToDatabaseAndMakeANewCard())
    sqlCodeButton.grid(row=12)

    newUserScreen.mainloop()

#Make a new screen that displays user Data to give new code DONE
def showUserData(id):
    showUserDataScreen = Tk()

    #Variables
    userId = id
    addressId = int()
    information = ""

    #Create a new code and add it to a RFID card
    def createCode(information):
        print(information)
        reader = SimpleMFRC522.SimpleMFRC522()
        dataString = information
        randomDataString = ''.join([random.choice(dataString) for _ in range(48)])

        print("Now place your tag to write")
        reader.write(randomDataString)
        print("Written")

        #Update the code to the database
        cursor = cnx.cursor(buffered=True)
        query = ("UPDATE `user` SET `code` = '{}' WHERE user.user_id = {}".format(randomDataString, userId))

        cursor.execute(query)
        cnx.commit()
        cursor.close()

    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')

    # Getting user data from database
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT firstname, lastname, email, username, code, address_id, user_id  FROM user WHERE {} = user_id".format(userId))
    cursor.execute(query)

    #Show user data on screen
    for (firstname, lastname, email, username, code, address_id, user_id) in cursor:
        #Variables
        firstName = firstname
        lastName = lastname
        eMail = email
        userName = username
        RFIDcode = code
        addressId = address_id

        #User details
        labelNaam = Label(showUserDataScreen, text="Voormaan")
        labelAchternaam = Label(showUserDataScreen, text="Achternaam")
        labelEmailadres = Label(showUserDataScreen, text="Email")
        labelGebruikersnaam = Label(showUserDataScreen, text="Gebruikersnaam")
        labelKaartcode = Label(showUserDataScreen, text="Kaartcode")

        labelNaam.grid(row=0, sticky=E)
        labelAchternaam.grid(row=1, sticky=E)
        labelEmailadres.grid(row=2, sticky=E)
        labelGebruikersnaam.grid(row=3, sticky=E)
        labelKaartcode.grid(row=4, sticky=E)

        naam = Label(showUserDataScreen, text=firstName)
        achternaam = Label(showUserDataScreen, text=lastName)
        emailadres = Label(showUserDataScreen, text=eMail)
        gebruikersnaam = Label(showUserDataScreen, text=userName)
        kaartcode = Label(showUserDataScreen, text=RFIDcode)

        naam.grid(row=0, column=1, sticky=W)
        achternaam.grid(row=1, column=1, sticky=W)
        emailadres.grid(row=2, column=1, sticky=W)
        gebruikersnaam.grid(row=3, column=1, sticky=W)
        kaartcode.grid(row=4, column=1, sticky=W)

        information = "{}{}{}{}{}{}{}".format(information, firstName, lastName, eMail, userName, RFIDcode, addressId)
        cursor.close()

    #Empty line so it looks better
    empty = Label(showUserDataScreen)
    empty.grid(row=5)

    #Getting user address data from database
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT street_address, zipcode, city  FROM address WHERE {} = address_id".format(addressId))
    cursor.execute(query)

    # Show user address on screen
    for (street_address, zipcode, city) in cursor:
        #Variables
        straat = street_address
        postcode = zipcode
        stad = city

        #User details
        labelStraat = Label(showUserDataScreen, text="Straat en nummer")
        labelPostcode = Label(showUserDataScreen, text="Postcode")
        labelStad = Label(showUserDataScreen, text="Stad")

        labelStraat.grid(row=6, sticky=E)
        labelPostcode.grid(row=7, sticky=E)
        labelStad.grid(row=8, sticky=E)

        street = Label(showUserDataScreen, text=straat)
        post = Label(showUserDataScreen, text=postcode)
        city = Label(showUserDataScreen, text=stad)

        street.grid(row=6, column=1, sticky=W)
        post.grid(row=7, column=1, sticky=W)
        city.grid(row=8, column=1, sticky=W)

        information = "{}{}{}{}".format(information, straat, postcode, stad)
        cursor.close()

    #Make a button that gives then a new code
    codeButton = Button(showUserDataScreen, text="Gegereer nieuwe code", command= lambda: createCode(information))
    codeButton.grid(row=9)

    showUserDataScreen.mainloop()

#Choose a user to give a new code DONE
def newCode():
    #Make a new screen
    newCodeScreen = Tk()

    #Show all customers
    # Making a connection with the database
    cnx = mysql.connector.connect(user='root',
                                  password='Benno',
                                  host='xxx.xxx.xxx.xxx',
                                  database='db3242919')

    # Getting data from database
    cursor = cnx.cursor(buffered=True)
    query = ("SELECT firstname, lastname, user_id  FROM user")
    cursor.execute(query)

    #Make all customers a button that loads their data
    for (firstname, lastname, user_id) in cursor:
        userButton = Button(newCodeScreen, text="{} {}".format(firstname, lastname), command= lambda user_id=user_id: showUserData(user_id))
        userButton.pack()
    cursor.close()

    newCodeScreen.mainloop()

#Show main screen DONE
def main():
    root = Tk()
    root.geometry("300x100")

    aantalPersonenButton = Button(text="Aantal personen in de sportschool", command=aantalPersonenScherm)
    aantalPersonenButton.pack()

    newUserButton = Button(text="Nieuwe gebruiker", command=newUser)
    newUserButton.pack()

    newCodeButton = Button(text="Nieuwe code", command=newCode)
    newCodeButton.pack()

    root.mainloop()

main()
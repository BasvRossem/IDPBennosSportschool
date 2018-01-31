#!/usr/bin/env python
import random
import RPi.GPIO as GPIO
import SimpleMFRC522
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

root = Tk() #Create a blank window
topFrame = Frame(root)
topFrame.pack()

def showDetails():
    reader = SimpleMFRC522.SimpleMFRC522()
    dataString = (voorletterEntry.get() + tussenvoegselEntry.get() + achternaamEntry.get() + geboortedatumEntry.get() + straatEntry.get() + huisnummerEntry.get() + toevoegingEntry.get() + postcodeEntry.get() + woonplaatsEntry.get())
    randomDataString = "".join(random.sample(dataString, 20))
    print("Now place your tag to write")
    reader.write(randomDataString)
    print("Written")
    GPIO.cleanup()

#Persoonlijke gegevens
voorletter = Label(topFrame, text="Voorletter(s)")
tussenvoegsel = Label(topFrame, text="Tussenvoegsel(s)")
achternaam = Label(topFrame, text="Achternaam")
geboortedatum = Label(topFrame, text="Geboortedatum")

voorletterEntry = Entry(topFrame)
tussenvoegselEntry = Entry(topFrame)
achternaamEntry = Entry(topFrame)
geboortedatumEntry = Entry(topFrame)

voorletter.grid(row=0, sticky=E)
tussenvoegsel.grid(row=1, sticky=E)
achternaam.grid(row=2, sticky=E)
geboortedatum.grid(row=3, sticky=E)

voorletterEntry.grid(row=0, column=1)
tussenvoegselEntry.grid(row=1, column=1)
achternaamEntry.grid(row=2, column=1)
geboortedatumEntry.grid(row=3, column=1)

#Tussenstreep
tussen = Label(topFrame)
tussen.grid(row=4)

#Adres
postcode = Label(topFrame, text="Postcode")
huisnummer = Label(topFrame, text="Huisnummer")
toevoeging = Label(topFrame, text="Toevoeging")
straat = Label(topFrame, text="Straat")
woonplaats = Label(topFrame, text="Woonplaats")

postcodeEntry = Entry(topFrame)
huisnummerEntry = Entry(topFrame)
toevoegingEntry = Entry(topFrame)
straatEntry = Entry(topFrame)
woonplaatsEntry = Entry(topFrame)

postcode.grid(row=5, sticky=E)
huisnummer.grid(row=6, sticky=E)
toevoeging.grid(row=7, sticky=E)
straat.grid(row=8, sticky=E)
woonplaats.grid(row=9, sticky=E)

postcodeEntry.grid(row=5, column=1)
huisnummerEntry.grid(row=6, column=1)
toevoegingEntry.grid(row=7, column=1)
straatEntry.grid(row=8, column=1)
woonplaatsEntry.grid(row=9, column=1)

#Button to show info
submitButton = Button(topFrame, text="Submit", command=showDetails)
submitButton.grid(row=10, columnspan=2)




root.mainloop() #This makes sure that the window stays on the screen

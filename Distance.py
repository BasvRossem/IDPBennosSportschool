import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 26
ECHO = 20

GPIO.setup(26,GPIO.OUT)
GPIO.output(26,0)

GPIO.setup(20,GPIO.IN)

while True:
    time.sleep(0.1)

    print("Starting Measurement")

    GPIO.output(26,1)
    time.sleep(0.00001)
    GPIO.output(26,0)

    while GPIO.input(20) == 0:
        pass
    start = time.time()

    while GPIO.input(20) == 1:
        pass
    stop = time.time()

    print ((stop-start)*170)*100 , " cm"
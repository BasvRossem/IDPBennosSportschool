import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
    while True:
        choose = raw_input("Choose 1, 2 or 3:")
        if choose == "1": #Neutral
            p.ChangeDutyCycle(7.5)
        elif choose == "2": #180
            p.ChangeDutyCycle(12.5)
        elif choose == "2":  # 180
            p.ChangeDutyCycle(2.5)
        else:
            break

finally:
    GPIO.cleanup()
import RPi.GPIO as GPIO
from time import sleep

v = (input("Hello, Would you like your medication dispensed?(Y/N): "))
if v in ['y', 'Y']:
    c = float(input("Which medication would you like dispensed?: "))
    if c == 1:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7,GPIO.OUT)

        pwm=GPIO.PWM(7,50)
        pwm.start(0)

        pwm.ChangeDutyCycle(5) #left
        sleep(1)
        #pwm.ChangeDutyCycle(7.5) # neutral position not neeeded since its a 360deg servo
        #sleep(1)
        pwm.ChangeDutyCycle(12.5) # right
        sleep(1)

        pwm.stop()
        GPIO.cleanup()

    elif c == 2:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)

        pwm=GPIO.PWM(11,50)
        pwm.start(0)

        pwm.ChangeDutyCycle(5) #left
        sleep(1)
        pwm.ChangeDutyCycle(12.5) # right 
        sleep(1)

        pwm.stop()
        GPIO.cleanup()

    elif c == 3:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13,GPIO.OUT)

        pwm=GPIO.PWM(13,50)
        pwm.start(0)

        pwm.ChangeDutyCycle(5) #left
        sleep(1)
        pwm.ChangeDutyCycle(10) # right
        sleep(1)

        pwm.stop()
        GPIO.cleanup()
        
    elif c == 4:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(15,GPIO.OUT)

        pwm=GPIO.PWM(15,50)
        pwm.start(0)

        pwm.ChangeDutyCycle(5) #left 
        sleep(1)
        pwm.ChangeDutyCycle(10) # right 
        sleep(1)

        pwm.stop()
        GPIO.cleanup()
        
    else:
        print("Sorry not available, Have a great day")
else :
    print("Thank you have a great day :) ")
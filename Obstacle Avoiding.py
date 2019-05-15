from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)                    #Set GPIO pin numbering

def ultrasonic():  
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    TRIG = 26                                 #Associate pin 23 to TRIG
    ECHO = 19                                 #Associate pin 24 to ECHO

    print("Distance measurement in progress")

    GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
   
    while True:
        GPIO.output(TRIG, False)                 #Set TRIG as LOW
        time.sleep(1)                           

        GPIO.output(TRIG, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                      #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                 #Set TRIG as LOW

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()              #Saves the last known time of LOW pulse

        while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
  
        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)            #Round to two decimal points
  
        if distance > 2 and distance < 400:
           print(distance - 0.5)  #Print distance with 0.5 cm calibration
           if (distance)<=20:
               GPIO.output(4,False)
               GPIO.output(25,True)
               GPIO.output(17,True)
               GPIO.output(18,False)
           else:
               GPIO.output(4,True)
               GPIO.output(25,False)
               GPIO.output(17,True)
               GPIO.output(18,False)
         else:
            print("Out Of Range")                   #display out of range

ultrasonic()

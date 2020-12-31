# Utlrasonic distance sensor:
# Max distance: 4 meters = 400 cm
# Min distacne: 20 mm = 0.2 cm

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#setting GPIO Pins
TRIG = 4
ECHO = 18

#setting Pins direction
GPIO.setup(TRIG, GPIO.OUT) #triggers the signal which will be reflected from the object
GPIO.setup(ECHO, GPIO.IN) #and then gets received from the echo pin

def debugg_time():
     #-----------triggering a very short signal for the measurement---------------
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    
    #----------setting the time frame for the measurement-----------
    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    delta_time = end-start #the time frame, in which the distance is being measured
    
    return delta_time

def distance():
    
    #-----------triggering a very short signal for the measurement---------------
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)
    
    #----------setting the time frame for the measurement-----------
    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
        
    delta_time = end-start #the time frame, in which the distance is being measured
    
    #-----------Measuring distance in cm----------------
    distance = delta_time*(343*100/2)
    #Sonic speed = 343m/s, measuring in cm (*100),
    #echo travels the distance twice (/2).

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            signal_span = debugg_time()
            print("Distance: %.1f cm" % dist) #printing out the distance value.
            print("Signal-Timespan: %f s" % signal_span) #for debugging: timespan of each distance measuremnt will be displayed
            time.sleep(1) #distance (and time) will be displayed every 1 second.
            
            
    except KeyboardInterrupt:
            rint("Measurement stopped by user")
            GPIO.cleanup()

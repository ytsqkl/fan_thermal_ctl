#coding=utf-8
#!/usr/bin/python
import sys
import time
try:
	import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        return float(f.read())/1000
def main():
    # Simplex use BCM-->4 pin control the fan 
    channel1 = 4
    # Duplex use BCM-->17 pin control the fan
    channel2 = 17



    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # close air fan first
    GPIO.setup(channel1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(channel2, GPIO.OUT, initial=GPIO.LOW)
    pwm1 = GPIO.PWM(channel1,100)
    pwm2 = GPIO.PWM(channel2,100)
    GPIO.setwarnings(False)
    is_close = True
    while True:
        temp = cpu_temp()
        if is_close:
            if temp > 42.0:
                print(time.ctime(), temp, '℃ open air fan')
                #GPIO.output(channel1, 1)
                #GPIO.output(channel2, 1)
                pwm1.start(0)
                pwm1.ChangeDutyCycle(100)
                pwm2.start(0)
                pwm2.ChangeDutyCycle(100)
                is_close = False
        else:
            if temp < 38.0:
                print(time.ctime(), temp, '℃ close air fan')
                #GPIO.output(channel1, 0)
                #GPIO.output(channel2, 0)
                pwm1.stop()
                pwm2.stop()
                is_close = True
        time.sleep(2.0)
        print(time.ctime(), temp, '℃')
if __name__ == '__main__':
    main()

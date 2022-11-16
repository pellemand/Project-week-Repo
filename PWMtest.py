#PWM test
import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 13
SpeedPin1 = 15
SpeedPin2 = 22
SpeedPin3 = 29
# PWM pins

dcForward = 100
dcBackward = -100
dcDriveRightWheels = 50
dcDriveLeftWheels = 50
dcStop = 0


DirectionPin = 11
DirectionPin1 = 16
DirectionPin2 = 18
DirectionPin3 = 31

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(SpeedPin1,GPIO.OUT)
GPIO.setup(SpeedPin2,GPIO.OUT)
GPIO.setup(SpeedPin3,GPIO.OUT)

GPIO.setup(DirectionPin,GPIO.OUT)
GPIO.setup(DirectionPin1,GPIO.OUT)
GPIO.setup(DirectionPin2,GPIO.OUT)
GPIO.setup(DirectionPin3,GPIO.OUT)


pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)

pi_pwm2 = GPIO.PWM(SpeedPin2,1000)		#create PWM instance with frequency
pi_pwm2.start(0)

pi_pwm3 = GPIO.PWM(SpeedPin3,1000)		#create PWM instance with frequency
pi_pwm3.start(0)

GPIO.output(DirectionPin, True)
GPIO.output(DirectionPin1, True)
GPIO.output(DirectionPin2, True)
GPIO.output(DirectionPin3, True)



def Forward(inputFromUser):
    inputFromUser = str(input())

    if inputFromUser == "w":
        pi_pwm.ChangeDutyCycle(dcForward)
        pi_pwm1.ChangeDutyCycle(dcForward)
        pi_pwm2.ChangeDutyCycle(dcForward)
        pi_pwm3.ChangeDutyCycle(dcForward)
        
def Backward(inputFromUser):
    inputFromUser = str(input())

    if inputFromUser == "s":
        pi_pwm.ChangeDutyCycle(dcBackward)
        pi_pwm1.ChangeDutyCycle(dcBackward)
        pi_pwm2.ChangeDutyCycle(dcBackward)
        pi_pwm3.ChangeDutyCycle(dcBackward)

def TurnLeft(inputFromUser):
    inputFromUser = str(input())

    if inputFromUser == "a":
        pi_pwm.ChangeDutyCycle(dcDriveLeftWheels)
        pi_pwm1.ChangeDutyCycle(dcDriveLeftWheels)
        pi_pwm2.ChangeDutyCycle(dcDriveRightWheels)
        pi_pwm3.ChangeDutyCycle(dcDriveRightWheels)

def TurnRight():
    inputFromUser = str(input())

    if inputFromUser == "d":
        pi_pwm.ChangeDutyCycle(dcDriveRightWheels)
        pi_pwm1.ChangeDutyCycle(dcDriveRightWheels)
        pi_pwm2.ChangeDutyCycle(dcDriveLeftWheels)
        pi_pwm3.ChangeDutyCycle(dcDriveLeftWheels)

# start PWM of required Duty Cycle 
while True:

    inputFromUser = input()
    for i in range(100):
        match inputFromUser:
            case "w":
                Forward(inputFromUser)
            case "s":
                Backward(inputFromUser)
            case "a":
                TurnLeft(inputFromUser)
            case "d":
                TurnRight(inputFromUser)
            case _:
                print("idfk")

    

         


    # for duty in range(0,101,1):
    #     pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
    #     pi_pwm1.ChangeDutyCycle(duty)
    #     pi_pwm2.ChangeDutyCycle(duty)
    #     pi_pwm3.ChangeDutyCycle(duty)
    #     sleep(0.1)
                
    # for duty in range(100,0,-1):
    #     pi_pwm.ChangeDutyCycle(duty)
    #     pi_pwm1.ChangeDutyCycle(duty)
    #     pi_pwm2.ChangeDutyCycle(duty)
    #     pi_pwm3.ChangeDutyCycle(duty)
    #     sleep(0.1)

    
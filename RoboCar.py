<<<<<<< HEAD
<<<<<<< HEAD
hej med dig
fmdksalæfjdksla
fdsa
fds
afd
saf
dsaf
dsaa
=======
# gpio17 = dir 1
# gpio27 = pwm1
# gpio22 = pwm2
# gpio23 = dir 2



# gpio24 = dir 1
# gpio25 = pwm1
# gpio05 = pwm2
# gpio06 = dir 2
>>>>>>> 9f904590ca3ee8610d3c15fbb22aa7226a52f8d3
=======
# gpio17 = 11 = dir 1
# gpio27 = 13 = pwm1
# gpio22 = 15 =  pwm2
# gpio23 = 16 = dir 2

# gpio24 = 18 = dir 1
# gpio25 = 22 = pwm1
# gpio05 = 29 = pwm2
# gpio06 = 31 = dir 2


# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY
GPIO.setup(15, GPIO.OUT) # Connected to BIN1
GPIO.setup(16, GPIO.OUT) # Connected to BIN2
GPIO.setup(18, GPIO.OUT) # Connected to PWMB

# Drive the motor clockwise
# Motor A:
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.HIGH) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
# Motor A:
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.HIGH) # Set AIN2
# Motor B:
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.HIGH) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(18, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(12, GPIO.LOW) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(13, GPIO.LOW) # Set STBY
GPIO.output(15, GPIO.LOW) # Set BIN1
GPIO.output(16, GPIO.LOW) # Set BIN2
GPIO.output(18, GPIO.LOW) # Set PWMB
>>>>>>> Johan

'''
from socket import *
from picarx import Picarx
import threading
import time
import pygame # to get the horn sound
# Initialize pygame mixer (call this before using any mixer functions)
pygame.mixer.init()

# Load the horn sound file
horn_sound = pygame.mixer.Sound("horn_sound.mp3")  # Replace with the actual file name

# Create a UDP socket and bind it to the specified server address
mySock = socket(AF_INET, SOCK_DGRAM)
mySock.bind(('', 25565))

# Initialize the Picarx instance
px = Picarx()

# Flag to keep track of the movement state
moving = False

# Function to avoid obstacle
def avoid_obstacle(): #how do i know which side it should go?
    # Play the horn sound when an obstacle is detected
    horn_sound.play()
    px.stop()  # Stop the car
    px.set_dir_servo_angle(-35)  # Turn the direction servo to avoid obstacle
    time.sleep(1)  # Adjust as needed to turn for a certain duration
    px.set_dir_servo_angle(0)  # Reset the direction servo to the front
    time.sleep(0.5)  # Adjust as needed before resuming forward movement
    px.forward(30)  # Resume forward movement

# Function to handle communication with the client
def server_thread():
    while True:
        message, clientAddress = mySock.recvfrom(2048)
        command = message.decode().lower()
        print(command)
        mySock.sendto("got it".encode(), clientAddress)

        if command == "forward" and not moving:
            # Move forward with obstacle avoidance
            while True:
                distance = px.ultrasonic_read()
                print("distance: ", distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        avoid_obstacle()
                    else:
                        px.turn_off_indicators()
                        px.set_dir_servo_angle(0)
                        px.forward(30)
                        moving = True
        elif command == "left" and not moving:
            px.turn_on_left_indicator()  # Turn on left indicator --figure this one out.
            px.set_dir_servo_angle(-35)  # Adjust angle as needed for left turn
            px.forward(30)
            moving = True
        elif command == "right" and not moving:
            px.turn_on_right_indicator()
            px.set_dir_servo_angle(35)  # Adjust angle as needed for right turn
            px.forward(30)
            moving = True
        elif command == "stop":
            px.stop()
            moving = False
        elif command == "circle" and not moving:
            # Move in a circle (adjust the angle and speed as needed)
            px.set_dir_servo_angle(-50)
            px.forward(30)
            moving = True

# Create a thread for the server
server_thread = threading.Thread(target=server_thread)
# Start the thread
server_thread.start()

'''

from robot_hat import TTS
from socket import *
from picarx import Picarx
import threading
import time
import pygame  # to get the horn sound

# Initialize pygame mixer (call this before using any mixer functions)
pygame.mixer.init()

# Load the horn sound file
horn_sound = pygame.mixer.Sound("horn_sound.wav")  # Replace with the actual file name

# Create a UDP socket and bind it to the specified server address
mySock = socket(AF_INET, SOCK_DGRAM)
mySock.bind(('', 25565))

# Initialize the Picarx instance
px = Picarx()

# Flag to keep track of the movement state
moving = False

# Function to avoid obstacle
def avoid_obstacle():
    # Play the horn sound when an obstacle is detected
    horn_sound.play()
    words = ["peeeeeeeeeeeep", "peeeeeeeeeeeep", "peeeeeeeeeeeep peeeeeeeeeeeep", "move out of way you dumb stupid beep"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)
    px.stop()  # Stop the car
    px.set_dir_servo_angle(-35)  # Turn the direction servo to avoid obstacle
    time.sleep(1)  # Adjust as needed to turn for a certain duration
    px.set_dir_servo_angle(0)  # Reset the direction servo to the front
    time.sleep(0.5)  # Adjust as needed before resuming forward movement
    px.forward(30)  # Resume forward movement

# Function to handle communication with the client
def server_thread():
    while True:
        global moving
        message, clientAddress = mySock.recvfrom(2048)
        command = message.decode().lower()
        print(command)
        mySock.sendto("got it".encode(), clientAddress)
        if command == "forward" and not moving:
            # Start a new thread for moving forward
            forward_thread = threading.Thread(target=move_forward)
            forward_thread.start()
        elif command == "left" and not moving:
            left_thread = threading.Thread(target=turn_left)
            left_thread.start()
        elif command == "right" and not moving:
            right_thread = threading.Thread(target=turn_right)
            right_thread.start()
        elif command == "backward" and not moving:
            backward_thread = threading.Thread(target=move_backward, args=(clientAddress,))
            backward_thread.start()
        elif command == "stop":
            px.stop()
            moving = False
        elif command == "circle" and not moving:
            circle_thread = threading.Thread(target=move_circle)
            circle_thread.start()
        elif command == "forward" and moving:
            px.stop()
            moving = False

def move_forward():
    global moving
    moving = True
    try:
        px.set_dir_servo_angle(0)
        while moving:
            distance = round(px.ultrasonic.read(), 2)
            print("distance: ", distance)
            if distance >= 40:
                px.forward(30)
            elif 20 <= distance < 40:
                px.set_dir_servo_angle(40)
                px.forward(30)
                time.sleep(0.1)
            else:
                avoid_obstacle()
                moving = True
    finally:
        moving = False
        px.forward(0)

def turn_left():
    global moving
    moving = True
    try:
        px.set_dir_servo_angle(-35)
        while moving:
            px.forward(30)
    finally:
        moving = False
        px.forward(0)

def turn_right():
    global moving
    moving = True
    try:
        px.set_dir_servo_angle(35)
        while moving:
            px.forward(30)
    finally:
        moving = False
        px.forward(0)

def move_backward(clientAddress):
    global moving
    moving = True
    try:
        while moving:
            px.backward(30)
    finally:
        moving = False
        px.backward(0)

def move_circle():
    global moving
    moving = True
    try:
        px.set_dir_servo_angle(-50)
        while moving:
            px.forward(30)
    finally:
        moving = False
        px.forward(0)

if __name__ == "__main__":
    server_thread()

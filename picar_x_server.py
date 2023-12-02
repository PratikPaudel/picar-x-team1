# Importing necessary modules to run the car
from socket import *
from picarx import Picarx
from vilib import Vilib
import pygame  # to get the horn sound
import os #to save the picture
import time
user = os.getlogin()
user_home = os.path.expanduser(f'~{user}')


# Initialize pygame mixer (call this before using any mixer functions)
pygame.mixer.init()

# Load the horn sound file
horn_sound = pygame.mixer.Sound("horn_sound.wav")
# Create a UDP socket and bind it to the specified server address
mySock = socket(AF_INET, SOCK_DGRAM)
mySock.bind(('', 25565))

# Initialize the Picarx instance
px = Picarx()

# Sets the speed to 30
speedd = 30
# Sets initial steering angle so that it starts straight
px.set_dir_servo_angle(-5.5)


# Function to handle communication with the client
def server_thread():
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False,web=True)
    path =f"{user_home}/picar-x/images"
    while True:
        global speedd

        # Receive a message and the client's address
        message, clientAddress = mySock.recvfrom(2048)
        command = message.decode().lower()

        print(command) # Prints the received command

        # Executions of the commands based on the received messages
        if command == "forward":
            px.forward(speedd)
        elif command == "notforward":
            px.forward(0)
        elif command == "left":
            px.set_dir_servo_angle(-29.5) # Setting angle when turning left
        elif command == "notleft":
            px.set_dir_servo_angle(-5.5)
        elif command == "right":
            px.set_dir_servo_angle(15) # Setting angle when turning right
        elif command == "notright":
            px.set_dir_servo_angle(-5.5)
        elif command == "backward":
            px.backward(speedd)
        elif command == "notbackward":
            px.backward(0)

        # Handles the camera movement
        if command == "a":
            px.set_camera_servo1_angle(-35)
        elif command == "nota":
            px.set_camera_servo1_angle(0)
        elif command == "d":
            px.set_camera_servo1_angle(35)
        elif command == "notd":
            px.set_camera_servo1_angle(0)
        elif command == "w":
            px.set_camera_servo2_angle(35)
        elif command == "notw":
            px.set_camera_servo2_angle(0)
        elif command == "s":
            px.set_camera_servo2_angle(-20)
        elif command == "nots":
            px.set_camera_servo2_angle(0)
        elif command == "h":
            horn_sound.play()
        elif command == "t":
            _time = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
            Vilib.take_photo(str(_time),path)
            print("The photo save as:%s/%s.jpg"%(path, _time))

        elif command == "speed": #Handles the speed command, sends and receives the input
            px.stop()
            speedmessage, clientAddress = mySock.recvfrom(2048)
            speedcommand = speedmessage.decode().lower()
            speedd = int(speedcommand)
            print(speedd)

# Entry point of the script
if __name__ == "__main__":
    server_thread()

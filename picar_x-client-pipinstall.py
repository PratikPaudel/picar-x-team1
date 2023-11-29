from socket import *
import keyboard

yourSock = socket(AF_INET, SOCK_DGRAM)

# Define functions to be called on key events
def on_left_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        #print("sending command left:")
        send_command('left')

def on_right_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('right')

def on_up_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('forward')

def on_down_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('stop')

def on_b_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('backward')

def on_s_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('speed')
        speed_select()

# Function to send commands to the server
def send_command(msg):
    yourSock.sendto(msg.encode(), ('ip', 25565))

# Function to change speed
def speed_select():
    speed = input("What speed would you like the robot to move (0-100): ")
    yourSock.sendto(speed.encode(), ('10.53.20.60', 25565))

# Bind the functions to the corresponding keys
keyboard.on_press_key('left', on_left_key)
keyboard.on_press_key('right', on_right_key)
keyboard.on_press_key('up', on_up_key)
keyboard.on_press_key('down', on_down_key)
keyboard.on_press_key('B', on_b_key)  # 'B' key for backward
keyboard.on_press_key('S', on_s_key)  # 'S' key for speed select

# Keep the program running
keyboard.wait()

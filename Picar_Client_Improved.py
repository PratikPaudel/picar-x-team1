from socket import *
import keyboard

yourSock = socket(AF_INET, SOCK_DGRAM)

# Define functions to be called on key events
def on_left_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('left')

def on_not_left_key(event):
    if event.event_type == keyboard.KEY_UP:
        send_command('notleft')

def on_right_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('right')

def on_not_right_key(event):
    if event.event_type == keyboard.KEY_UP:
        send_command('notright')

def on_up_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('forward')

def on_not_up_key(event):
    if event.event_type == keyboard.KEY_UP:
        send_command('notforward')

def on_down_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('backward')

def on_not_down_key(event):
    if event.event_type == keyboard.KEY_UP:
        send_command('notbackward')

def on_s_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        send_command('speed')
        speed_select()

# Function to send commands to the server
def send_command(msg):
    yourSock.sendto(msg.encode(), ('10.57.16.65', 25565))

# Function to change speed
def speed_select():
    try:
        speed = int(input("What speed would you like the robot to move (0-100): "))

        while((speed > 100) or (speed < 0)):
            speed = int(input("Invalid speed. What speed would you like the robot to move (0-100): "))
    except ValueError:
        print("Invalid entry type. Resetting robot speed to 30.")
        speed = "30"
        
    speed = str(speed)
    yourSock.sendto(speed.encode(), ('10.57.16.65', 25565))

# Bind the functions to the corresponding keys
keyboard.on_press_key('left', on_left_key)
keyboard.on_release_key('left', on_not_left_key)

keyboard.on_press_key('right', on_right_key)
keyboard.on_release_key('right', on_not_right_key)

keyboard.on_press_key('up', on_up_key)
keyboard.on_release_key('up', on_not_up_key)

keyboard.on_press_key('down', on_down_key)
keyboard.on_release_key('down', on_not_down_key)

keyboard.on_press_key('S', on_s_key)  # 'S' key for speed select

# Keep the program running
keyboard.wait()
